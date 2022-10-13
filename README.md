# Linear-Programming-Problem-Solver


--------------------------------------------------------------------------
L.H.S of Objective Function"s Coefficients  [1, -3, -2, -4, 0, 0, 0, 0]
R.H.S : [0, 9, 18, -18, -7]
Initial Basic Variables  ['s_1', 's_2', 's_3', 's_4']
L.H.S of Constraints" Coefficients :  [[0, 1, 1, 1, 1, 0, 0, 0], [0, 3, 1, 4, 0, 1, 0, 0], [0, -3, -1, -4, 0, 0, 1, 0], [0, -1, -2, 0, 0, 0, 0, 1]]
Basic Variables  ['s_1', 's_2', 's_3', 's_4']
Variables are  ['z', 'x_1', 'x_2', 'x_3', 's_1', 's_2', 's_3', 's_4']
table columns : ['z', 'x_1', 'x_2', 'x_3', 's_1', 's_2', 's_3', 's_4', 'rhs', 'BV']
---------------------------------------------------------------------------
Initial Stage ...
   z  x_1  x_2  x_3  s_1  s_2  s_3  s_4  rhs   BV
0  1   -3   -2   -4    0    0    0    0    0    z
1  0    1    1    1    1    0    0    0    9  s_1
2  0    3    1    4    0    1    0    0   18  s_2
3  0   -3   -1   -4    0    0    1    0  -18  s_3
4  0   -1   -2    0    0    0    0    1   -7  s_4
3 entering [[0, 1, 1, 1, 1, 0, 0, 0], [0, 3, 1, 4, 0, 1, 0, 0], [0, -3, -1, -4, 0, 0, 1, 0], [0, -1, -2, 0, 0, 0, 0, 1]]
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
     z   x_1   x_2  x_3  s_1   s_2  s_3  s_4   rhs   BV
0  1.0  0.00 -1.00  0.0  0.0  1.00  0.0  0.0  18.0    z
1  0.0  0.25  0.75  0.0  1.0 -0.25  0.0  0.0   4.5  s_1
2  0.0  0.75  0.25  1.0  0.0  0.25  0.0  0.0   4.5  x_3
3  0.0 -3.00 -1.00 -4.0  0.0  0.00  1.0  0.0 -18.0  s_3
4  0.0 -1.00 -2.00  0.0  0.0  0.00  0.0  1.0  -7.0  s_4
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
     z   x_1   x_2  x_3  s_1   s_2  s_3  s_4   rhs   BV
0  1.0  0.00 -1.00  0.0  0.0  1.00  0.0  0.0  18.0    z
1  0.0  0.25  0.75  0.0  1.0 -0.25  0.0  0.0   4.5  s_1
2  0.0  0.75  0.25  1.0  0.0  0.25  0.0  0.0   4.5  x_3
3  0.0  0.00  0.00  0.0  0.0  1.00  1.0  0.0   0.0  s_3
4  0.0 -1.00 -2.00  0.0  0.0  0.00  0.0  1.0  -7.0  s_4
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
     z   x_1   x_2  x_3  s_1   s_2  s_3  s_4   rhs   BV
0  1.0  0.00 -1.00  0.0  0.0  1.00  0.0  0.0  18.0    z
1  0.0  0.25  0.75  0.0  1.0 -0.25  0.0  0.0   4.5  s_1
2  0.0  0.75  0.25  1.0  0.0  0.25  0.0  0.0   4.5  x_3
3  0.0  0.00  0.00  0.0  0.0  1.00  1.0  0.0   0.0  s_3
4  0.0 -1.00 -2.00  0.0  0.0  0.00  0.0  1.0  -7.0  s_4
------------------------------------------------------------------------------------
2 entering [[0.0, 0.25, 0.75, 0.0, 1.0, -0.25, 0.0, 0.0], [0.0, 0.75, 0.25, 1.0, 0.0, 0.25, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0], [0.0, -1.0, -2.0, 0.0, 0.0, 0.0, 0.0, 1.0]]
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
     z       x_1  x_2  x_3       s_1       s_2  s_3  s_4   rhs   BV
0  1.0  0.333333  0.0  0.0  1.333333  0.666667  0.0  0.0  24.0    z
1  0.0  0.333333  1.0  0.0  1.333333 -0.333333  0.0  0.0   6.0  x_2
2  0.0  0.666667  0.0  1.0 -0.333333  0.333333  0.0  0.0   3.0  x_3
3  0.0  0.000000  0.0  0.0  0.000000  1.000000  1.0  0.0   0.0  s_3
4  0.0 -1.000000 -2.0  0.0  0.000000  0.000000  0.0  1.0  -7.0  s_4
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
     z       x_1  x_2  x_3       s_1       s_2  s_3  s_4   rhs   BV
0  1.0  0.333333  0.0  0.0  1.333333  0.666667  0.0  0.0  24.0    z
1  0.0  0.333333  1.0  0.0  1.333333 -0.333333  0.0  0.0   6.0  x_2
2  0.0  0.666667  0.0  1.0 -0.333333  0.333333  0.0  0.0   3.0  x_3
3  0.0  0.000000  0.0  0.0  0.000000  1.000000  1.0  0.0   0.0  s_3
4  0.0 -1.000000 -2.0  0.0  0.000000  0.000000  0.0  1.0  -7.0  s_4
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
     z       x_1  x_2  x_3       s_1       s_2  s_3  s_4   rhs   BV
0  1.0  0.333333  0.0  0.0  1.333333  0.666667  0.0  0.0  24.0    z
1  0.0  0.333333  1.0  0.0  1.333333 -0.333333  0.0  0.0   6.0  x_2
2  0.0  0.666667  0.0  1.0 -0.333333  0.333333  0.0  0.0   3.0  x_3
3  0.0  0.000000  0.0  0.0  0.000000  1.000000  1.0  0.0   0.0  s_3
4  0.0 -0.333333  0.0  0.0  2.666667 -0.666667  0.0  1.0   5.0  s_4
------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
Final Output
--------------------------------------------------------------------------------------

     z       x_1  x_2  x_3       s_1       s_2  s_3  s_4   rhs   BV
0  1.0  0.333333  0.0  0.0  1.333333  0.666667  0.0  0.0  24.0    z
1  0.0  0.333333  1.0  0.0  1.333333 -0.333333  0.0  0.0   6.0  x_2
2  0.0  0.666667  0.0  1.0 -0.333333  0.333333  0.0  0.0   3.0  x_3
3  0.0  0.000000  0.0  0.0  0.000000  1.000000  1.0  0.0   0.0  s_3
