

'''
BlandSimplex built to return an optimal basic feasible solution and its value
1. Simplex method - Bland Rule
2. Argument object holds
      an array of objective function coefficients
      right-hand side entries
      a  matrix of coefficients for the left-hand-sides of the constraints
3. The processor built to perform mostly on Maximization problem
4. It will add slack variable automaticall
'''
import pandas as pd

class StandardForm:
    def __init__(self):

        self.rhs = [0, 13, 41, 5, 1]
        self.basic_variables = ['s_1', 's_2', 's_3', 's_4']
        self.row_0_lhs = [1, -5, -7, 0, 0, 0, 0]
        self.rows_lhs = [[0, 2, 1, 1, 0, 0, 0], [0, 5, 9, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1]]
        self.variables = ['z', 'x_1', 'x_2', 's_1', 's_2', 's_3', 's_4']
        self.table_columns = ['z', 'x_1', 'x_2', 's_1', 's_2', 's_3', 's_4', 'rhs', 'BV']


class MaximizationSimplex:
    def __init__(self):

        self.stdform = StandardForm()
        print('--------------------------------------------------------------------------')
        print('L.H.S of Objective Function"s Coefficients ', self.stdform.row_0_lhs)
        print('R.H.S :', self.stdform.rhs)
        print('Initial Basic Variables ', self.stdform.basic_variables)
        print('L.H.S of Constraints" Coefficients : ', self.stdform.rows_lhs)
        print('Basic Variables ', self.stdform.basic_variables)
        print('Variables are ', self.stdform.variables)
        print('table columns :', self.stdform.table_columns )
        print('---------------------------------------------------------------------------')

        print('Initial Stage ...')

        table_rows = [self.stdform.row_0_lhs + [self.stdform.rhs[0]] + ['z']] + [
            self.stdform.rows_lhs[i] + [self.stdform.rhs[i + 1]] + [self.stdform.basic_variables[i]]
            for i in range(len(self.stdform.rows_lhs))]

        df = pd.DataFrame(table_rows,
                          columns=self.stdform.table_columns)
        df.style.set_properties(**{'text-align': 'center'})

        print(df)

        self._to_positive_objfun()

    def substraction_op(self, indx, multiplied_row_0, multiplied_pivot_row):
        return multiplied_row_0[indx] + multiplied_pivot_row[indx]


    def fetch_pivot_row(self, entering_idx):

        MIN = 0
        pivot_row = list()
        leaving_row_indx = 0
        idnx = 0
        for r_indx, r_coef in enumerate(self.stdform.rows_lhs):
            #print("row ", r_coef, "coef", r_coef[entering_idx], 'row"s index', r_indx, 'rhs value ', self.stdform.rhs[r_indx + 1])
            if r_coef[entering_idx] > 0:  # coefficient in l.h.s should be greater than 0
                ratio = round(self.stdform.rhs[r_indx + 1] / r_coef[entering_idx], 2)
                if idnx == 0:
                    MIN = ratio
                    pivot_row = r_coef
                    leaving_row_indx = r_indx
                else:
                    if ratio < MIN:
                        pivot_row = r_coef
                        MIN = ratio
                        leaving_row_indx = r_indx
                idnx += 1
        #print(MIN, pivot_row , leaving_row_indx, self.stdform.basic_variables[leaving_row_indx])
        if pivot_row:
            return MIN, pivot_row , leaving_row_indx, self.stdform.basic_variables[leaving_row_indx]

    def calculate_ratio_quantities_replacements(self, entering_idx):

        fetched_details = self.fetch_pivot_row(entering_idx)
        if fetched_details:
            MIN, initial_pivot_row, leaving_row_indx, leaving_var = fetched_details

            self.stdform.rhs[leaving_row_indx + 1] = round(self.stdform.rhs[leaving_row_indx + 1] / initial_pivot_row[entering_idx], 2)
            pivot_row = [__p/initial_pivot_row[entering_idx] for __p in  initial_pivot_row]

            self.stdform.rows_lhs[leaving_row_indx] = pivot_row

            pivot = pivot_row[entering_idx]


            entering_value = self.stdform.row_0_lhs[entering_idx]
            #print('-------------------------------------------------------------------')
            #print('Minimum ratio :',  MIN, 'Pivot"s row :', pivot_row,'Pivot :',pivot, 'Leaving variable"s index', leaving_row_indx,
                  #'Leaving variable :',leaving_var, "Entering Varaible's index :" , entering_idx," Entering Variable : " , ( self.stdform.variables[entering_idx] ,entering_value))
            #print('--------------------------------------------------------------------')
            #########
            #self.tabluea_calculations()
            multiplied_row_0  = [__i * pivot  for __index, __i in enumerate(self.stdform.row_0_lhs)]
            multiplied_pivot_row = [__i * entering_value for __index, __i in enumerate(pivot_row)]

            rhs_z_multiply = self.stdform.rhs[0] * pivot
            rhs_pivot_multply = self.stdform.rhs[leaving_row_indx + 1] * entering_value

            if sum([multiplied_pivot_row[entering_idx], multiplied_row_0[entering_idx]]) != 0:
                multiplied_pivot_row = [__i * -1 for __index, __i in enumerate(multiplied_pivot_row)]
                rhs_pivot_multply = rhs_pivot_multply * -1

            self.stdform.row_0_lhs = [self.substraction_op(__i, multiplied_row_0, multiplied_pivot_row) for __i in range(len(self.stdform.row_0_lhs))]

            self.stdform.rhs[0] = rhs_z_multiply + rhs_pivot_multply


            self.stdform.basic_variables[leaving_row_indx] = self.stdform.variables[entering_idx] # s2 leaves = enters x1

            #######
            for __rindex, __rs in enumerate(self.stdform.rows_lhs):

                if __rindex == leaving_row_indx:
                    #print('PIVOT"s Row ', pivot_row)
                    continue


                multiplied_neighbour_row = [ __i * pivot  for __index, __i in enumerate(__rs)]
                multiplied_pivot_row  = [__i *  __rs[entering_idx] for __index, __i in enumerate(pivot_row)]


                rhs_z_multiply = self.stdform.rhs[__rindex + 1] * pivot
                rhs_pivot_multply = self.stdform.rhs[leaving_row_indx + 1] * __rs[entering_idx]
                #print(rhs_z_multiply, rhs_pivot_multply)

                if sum([multiplied_neighbour_row[entering_idx], multiplied_pivot_row[entering_idx]]) != 0:

                    multiplied_pivot_row = [__i * -1 for __index, __i in enumerate(multiplied_pivot_row)]
                    rhs_pivot_multply = rhs_pivot_multply * -1

                self.stdform.rows_lhs[__rindex] = [self.substraction_op(__i, multiplied_neighbour_row, multiplied_pivot_row) for __i in range(len(__rs))]

                self.stdform.rhs[__rindex + 1] = rhs_z_multiply + rhs_pivot_multply
                print('-----------------------------------------------')

                table_rows = [self.stdform.row_0_lhs + [self.stdform.rhs[0]] + ['z']] + [
                    self.stdform.rows_lhs[i] + [self.stdform.rhs[i + 1]] + [self.stdform.basic_variables[i]]
                    for i in range(len(self.stdform.rows_lhs))]

                df = pd.DataFrame(table_rows,
                                  columns=self.stdform.table_columns)
                df.style.set_properties(**{'text-align': 'center'})

                print(df)
                print('-----------------------------------------------')
            return self.stdform.row_0_lhs
    def _to_positive_objfun(self):

        if [__v for __v in self.stdform.row_0_lhs if __v < 0]:
            coef_row0 = min(self.stdform.row_0_lhs)
            if coef_row0 < 0:
                entering_idx = self.stdform.row_0_lhs.index(coef_row0)
                #print(entering_idx, 'entering', self.stdform.rows_lhs)
                res = self.calculate_ratio_quantities_replacements(entering_idx)
                if res == None:
                    print('---------------------------------------')
                    print('Final Output')
                    print('---------------------------------------')

                    print('UNBOUNDED LP')

                    table_rows = [self.stdform.row_0_lhs + [self.stdform.rhs[0]] + ['z']] + [ self.stdform.rows_lhs[i] + [self.stdform.rhs[i+1]] + [self.stdform.basic_variables[i]]
                                                                                       for i in range(len(self.stdform.rows_lhs)) ]

                    df = pd.DataFrame(table_rows,
                                      columns=self.stdform.table_columns)
                    df.style.set_properties(**{'text-align': 'center'})

                    print(df)
                else:
                    return self._to_positive_objfun()
        else:
            print("-----------------------------------------------")
            print('Final Output')
            print('-----------------------------------------------')

            print()

            table_rows = [self.stdform.row_0_lhs + [self.stdform.rhs[0]] + ['z']] + [
                self.stdform.rows_lhs[i] + [self.stdform.rhs[i + 1]] + [self.stdform.basic_variables[i]]
                for i in range(len(self.stdform.rows_lhs))]

            df = pd.DataFrame(table_rows,
                              columns=self.stdform.table_columns)
            df.style.set_properties(**{'text-align': 'center'})

            print(df)
            print('--------------------------------------------------------------------')

            print()


MaximizationSimplex()