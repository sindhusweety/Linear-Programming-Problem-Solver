'''
1. Simplex method
2. Argument object holds
      an array of objective function coefficients
      right-hand side entries
      a  matrix of coefficients for the left-hand-sides of the constraints
3. The processor built to perform mostly on Maximization problem
4. It will add slack variable automaticall
'''
import copy

import pandas as pd


class Arguments:
    def __init__(self):
        self.equations = ['x_1 + x_2 <= 6', 'x_1 - x_2 <= 0']
        self.obj_atrributes = [60, 30, 20]  # [5, 2] #an array of objective function coefficients----------5x_1 + 2x_2
        self.decision_variable_rhs = [48, 20, 8]  # [6, 0] # right-hand side entries
        self.decision_variable_lhs = [[8, 6, 1], [4, 2, 1.5], [2, 1.5, 0.5]]  # [[1, 1],[1, -1 ]] #coefficients for the left-hand-sides of the constraints
        self.no_equations = len(self.decision_variable_lhs)
        self.no_variables = len(self.decision_variable_lhs[0])
        self.lowbound = "x1, x2 >= 0"

def add_slack_variables(len, arr):
    return arr +  [ 0 for i in range(len)]


class ConvertIntoStandardForm:
    def __init__(self):
        self.obj = Arguments()
        self.z_cof = 1 #Z coefficient -----------Always 1 initially
        self.rhs = [0] + self.obj.decision_variable_rhs #add z = 0 initially in the right hand side
        self.basic_variables = ['s_'+str(index+1)  for index, i in enumerate(self.rhs[1:])] #Initially s_1, s_2
        self.row_0_lhs = add_slack_variables( self.obj.no_equations, [self.z_cof] + [ -1 * r0 for r0 in self.obj.obj_atrributes]) #setting slack values initially to Objective function row
        self.rows_lhs = [ [0] + add_slack_variables(self.obj.no_equations, cof)    for cof in (self.obj.decision_variable_lhs)] #setting slack values to constraints initially
        for idx , cof in enumerate(self.rows_lhs):
            cof[ self.obj.no_variables + idx + 1] = 1  # 10
                                                       # 01
        self.variables = ['z'] + ['x_'+str(i+1) for i in range(self.obj.no_variables)] + self.basic_variables
        self.table_columns = self.variables + ['rhs', 'BV']


class MaxSimplexMethod:
    def __init__(self):
        self.obj = Arguments()
        self.stdform = ConvertIntoStandardForm()
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

        #self._to_positive_objfun()

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
                print('------------------------------------------------------------------------------------')
                print('------------------------------------------------------------------------------------')
                table_rows = [self.stdform.row_0_lhs + [self.stdform.rhs[0]] + ['z']] + [
                    self.stdform.rows_lhs[i] + [self.stdform.rhs[i + 1]] + [self.stdform.basic_variables[i]]
                    for i in range(len(self.stdform.rows_lhs))]

                df = pd.DataFrame(table_rows,
                                  columns=self.stdform.table_columns)
                df.style.set_properties(**{'text-align': 'center'})

                print(df)
                print('------------------------------------------------------------------------------------')
            return self.stdform.row_0_lhs
    def _to_positive_objfun(self):

        if [__v for __v in self.stdform.row_0_lhs if __v < 0]:
            coef_row0 = min(self.stdform.row_0_lhs)
            if coef_row0 < 0:
                entering_idx = self.stdform.row_0_lhs.index(coef_row0)
                #print(entering_idx, 'entering', self.stdform.rows_lhs)
                res = self.calculate_ratio_quantities_replacements(entering_idx)
                if res == None:
                    print('------------------------------------------------------------------------------------')
                    print('Final Output')
                    print('------------------------------------------------------------------------------------')

                    print('UNBOUNDED LP')

                    table_rows = [self.stdform.row_0_lhs + [self.stdform.rhs[0]] + ['z']] + [ self.stdform.rows_lhs[i] + [self.stdform.rhs[i+1]] + [self.stdform.basic_variables[i]]
                                                                                       for i in range(len(self.stdform.rows_lhs)) ]

                    df = pd.DataFrame(table_rows,
                                      columns=self.stdform.table_columns)
                    df.style.set_properties(**{'text-align': 'center'})
                    print(df)
                    return df
                else:
                    return self._to_positive_objfun()
        else:
            print("--------------------------------------------------------------------------------------")
            print('Final Output')
            print('--------------------------------------------------------------------------------------')

            print()

            table_rows = [self.stdform.row_0_lhs + [self.stdform.rhs[0]] + ['z']] + [
                self.stdform.rows_lhs[i] + [self.stdform.rhs[i + 1]] + [self.stdform.basic_variables[i]]
                for i in range(len(self.stdform.rows_lhs))]

            df = pd.DataFrame(table_rows,
                              columns=self.stdform.table_columns)
            df.style.set_properties(**{'text-align': 'center'})
            print(df)
            return df

class SensitivityAnalysis:
    def __init__(self):

        self.__final_tableau   = MaxSimplexMethod()._to_positive_objfun()

        self.__standform = ConvertIntoStandardForm()
        print('--------------------------------------------------------------------------')
        print('L.H.S of Objective Function"s Coefficients ', self.__standform.row_0_lhs)
        print('R.H.S :', self.__standform.rhs)
        print('Initial Basic Variables ', self.__standform.basic_variables)
        print('L.H.S of Constraints" Coefficients : ', self.__standform.rows_lhs)
        print('Basic Variables ', self.__standform.basic_variables)
        print('Variables are ', self.__standform.variables)
        print('table columns :', self.__standform.table_columns)
        table_rows = [self.__standform.row_0_lhs + [self.__standform.rhs[0]] + ['z']] + [
            self.__standform.rows_lhs[i] + [self.__standform.rhs[i + 1]] + [self.__standform.basic_variables[i]]
            for i in range(len(self.__standform.rows_lhs))]

        df = pd.DataFrame(table_rows, columns=self.__standform.table_columns)
        self.__Xbv = self.__final_tableau['BV'][1:].values.tolist()
        self.__Xnbv = [ nbv for nbv in self.__standform.variables  if nbv not in self.__final_tableau['BV'].values.tolist()]
        self.__Cbv = [ abs(df[bv][0]) if df[bv][0] <=0 else -df[bv][0]  for bv in self.__Xbv  ]
        self.__Cnbv = [abs(df[bv][0]) if df[bv][0] <=0 else -df[bv][0] for bv in self.__Xnbv]
        self._B_inverse = [self.__final_tableau[s].values.tolist()[1:] for s in self.__standform.basic_variables ]
        self._B_X = [s for s in self.__standform.variables[1:] if s not in self.__standform.basic_variables]
        self._B_Inverse_Aj = [self.__final_tableau[nbv].values.tolist()[1:] for nbv in self.__Xnbv ]
        self.__rhs =self.__standform.rhs[1:]
        print(self._B_inverse)
        print(self._B_Inverse_Aj)



        self.changes_objective_function_basics()
        self.changes_objective_function_nonbasics()
        self.changes_rhs()

    def CbBinverseAj_multiplication(self, added_delta, bvindex, bv):
        matrixCbBinv = [[]  for i in range(len(added_delta))]
        deltaval = list()
        for row in range(len(added_delta)):
            for col in range(len(self._B_Inverse_Aj)):
                if bvindex == row:
                    matrixCbBinv[col].append(added_delta[row][0] * self._B_Inverse_Aj[col][row])
                    deltaval.append(added_delta[row][1] * self._B_Inverse_Aj[col][row])
                else:
                    Aij = added_delta[row] * self._B_Inverse_Aj[col][row]
                    if abs(Aij) == 0:
                        matrixCbBinv[col].append(abs(Aij))
                    else:
                        matrixCbBinv[col].append(Aij)

        for i in range(len(matrixCbBinv)):
            matrixCbBinv[i] = [(sum(matrixCbBinv[i]))]
            matrixCbBinv[i].append(deltaval[i])

        return matrixCbBinv

    def __finddeltaranges(self, matrixCbBinv):

        deltanegativerange = list()
        deltapositiverange = list()
        for i in range(len(matrixCbBinv)):
            if matrixCbBinv[i][0] > 0:

                deltarange = -matrixCbBinv[i][0]/ matrixCbBinv[i][1]
                if deltarange > 0:
                    deltapositiverange.append(deltarange)
                else:
                    deltanegativerange.append(deltarange)

            else:
                deltarange = matrixCbBinv[i][0] / matrixCbBinv[i][1]
                if deltarange > 0:
                    deltapositiverange.append(deltarange)
                else:
                    deltanegativerange.append(deltarange)
        if deltanegativerange and not deltapositiverange:
            return max(deltanegativerange), ''
        elif not deltanegativerange and deltapositiverange:
            return '', max(deltapositiverange)
        elif deltanegativerange and deltapositiverange:
            return max(deltanegativerange), max(deltapositiverange)

    def subtractCnbvFrmCbBinverse(self, matrixCbBinv):
        for n in range(len(self.__Cnbv)):
            matrixCbBinv[n][0] = matrixCbBinv[n][0] - self.__Cnbv[n]
        return matrixCbBinv

    def changes_objective_function_basics(self):

        for bvindex, bv in enumerate(self.__Cbv):
            if bv >0:
                added_delta = copy.deepcopy(self.__Cbv)
                added_delta[bvindex] = [bv, 1]

                matrixCbBinv = self.CbBinverseAj_multiplication(added_delta, bvindex, bv)
                matrixCbBinv =self.subtractCnbvFrmCbBinverse(matrixCbBinv)
                delta_range = self.__finddeltaranges(matrixCbBinv)
                added_delta[bvindex] = str(bv) + " + \u0394"
                print('----------------------------------------------------------------')
                print("Changing the objective function coefficient of a basic variable")
                print(delta_range[0], " <= \u0394 <=", delta_range[1], " for ", added_delta )
                if  not delta_range[0] and delta_range[1]:
                    print("Cbv <=", delta_range[1]+bv)
                elif delta_range[0] and not delta_range[1]:
                    print(delta_range[0]+bv, "<= Cbv")
                elif delta_range[0] and delta_range[1]:
                    print(delta_range[0]+bv, "<= C{number} <=".format(number=bvindex), delta_range[1]+bv)
                print('-----------------------------------------------------------------')


    def CbBinverseAj_multiply_subtract_Cnbv(self, bvindex, nbv):
        newDelta = 0
        for row in range(len(self.__Cbv)):
            Aij= self.__Cbv[row] * self._B_Inverse_Aj[bvindex][row]
            if abs(Aij) == 0:
                newDelta += abs(Aij)
            else:
                newDelta += Aij
        return newDelta - nbv
    def changes_objective_function_nonbasics(self):
        for bvindex, nbv in enumerate(self.__Cnbv):
            if nbv >0:
                newDelta = self.CbBinverseAj_multiply_subtract_Cnbv( bvindex, nbv)
                added_delta = copy.deepcopy(self.__Cnbv)
                added_delta[bvindex] = str(nbv) + "+ \u0394"
                if newDelta > 0:
                    print('-----------------------------------------------------------------')
                    print("Changing the objective function coefficient of a non basic variable")
                    print("\u0394 <= ", newDelta)
                    print("C{number}".format(number=bvindex), "for ",  added_delta)

                else:
                    print('-----------------------------------------------------------------')
                    print("Changing the objective function coefficient of a non basic variable")
                    print(newDelta,"<= \u0394")
                    print("C{number}".format(number=bvindex), "for ", added_delta)



    def changes_rhs(self):
        print(self.__rhs)
        


SensitivityAnalysis()

