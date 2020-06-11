import sys  # this allows you to use the sys.exit command to quit/logout of the application
import time
import turtle
import os
import numpy
import cv2

def main():
    option = input("Do you want to continue? Yes or No ")
    if option == "yes" or option == "Yes":
        os.system('cls')
        choice = input("""

                                Which one would you like to learn today?

         1. Reciprocal identities
         2. Pythagorean Identities
         3. Quotient Identities
         4. Negative/Opposite Angle Identities
         5. Even-Odd Identities
         6. Sum-Difference Formulas
         7. Double Angle Formulas
         8. Quiz  
             """)
        if choice == "Reciprocal identities" or choice == "Reciprocal" or choice == "1":
            print("""
           
                Now this is an exciting topic!!!
           
                  A matrix is a two dimensional array of numbers or expressions
                  typically written in brackets and arranged into a pattern
                   of rows and columns. An m * n matrix A has m rows and n
                     columns and is written: 
          
                              | a     b |                           
                         A =  | c     d |         or           B =  | a    b |
                              | e     f |                           | c    d |
                     
                     
                     The matrices above have dimensions: 
                     A => 2 * 3              B=>  2 * 2  
                     
                     Nb. If there are the same number of rows as columns, 
                     the matrix is square, otherwise it is a rectangular matrix. 
                     
            """)
            choice == input("""Now that we've set the foundation, let the games begin:
            
                                1. Game of Addition
                                2. Game of Scalar Multiplication 
                                3. Game of Matrix Multiplication
                                4. Game of Gaussian Elimination
                                """)
            if choice== "1":
                os.system('cls')
                print("""                                      Game of Addition
                                                                ****RULES****
                
                         Two matrices may be added or subtracted only if they have the same dimension; that is, they must
                         have the same number of rows and columns. For instance, you can't add, say, a 3×4 matrix 
                         to a 4×4 matrix, but you can add two 3×4 matrices. 
                         Addition or subtraction is accomplished by adding or subtracting corresponding elements. 
                        
                        
                        """)

                os.system('cls')
                print("""
                                             **** HERE'S AN EXAMPLE ****
                                       
                                      A        +         B     
                                |  2    -3 |       |  9     -5 |          | 11     -8 |
                                |  1     0 |   +   |  0     13 |     =    |  1     13 |
                                | -1     3 |       | -1      3 |          | -2      6 |
                 
                 
                 
                            GREAT NOW THAT YOU KNOW THE RULES RETURN TO THE MENU TO PLAY
                                                  
                """)
            if choice == "2":
                os.system('cls')
                print("""                                Game of Scalar Multiplication
                                                                ****RULES****

                         The term scalar multiplication refers to the product of a real number and a matrix. 
                         In scalar multiplication, each entry in the matrix is multiplied by the given scalar.


                         """)

                print("""
                                              
                                              **** HERES AN EXAMPLE ****

                        The manager of Kings's hardware store has trippled the production of paint.
                        Before this boost, the amount of paint produced weekly were:     
                                       
                                                            |  25 red     30 black  |               
                                                            |  35 blue    10 purple |       
                                                            |  17 pink    23 yellow |               

                        
                        
                        Now the revised quantities would be: 
                        
                              | 3 * 25 red      3 * 30 black  |                   | 25 red      30 black  |               
                              | 3 * 35 blue     3 * 10 purple |       or      3   | 35 blue     10 purple |
                              | 3 * 17 pink     3 * 23 yellow |                   | 17 pink     23 yellow |


                        This can be represented in matrix form as: 
                        
                                                                | 75        90 |
                                                                | 105       30 |
                                                                | 51        69 |


                        If A = m × n is a matrix and k is a scalar, then kA is another matrix which is obtained 
                        by multiplying each element of A by the scalar k.



                             GREAT NOW THAT YOU KNOW THE RULES RETURN TO THE MENU TO PLAY

                 """)

            if choice == "3":
                os.system('cls')
                print("""                                Game of Matrix Multiplication
                                                                ****RULES****

                         The product of two matrices is defined only when the number of columns of the first 
                         matrices is the same as the number of rows as the second.
                         Therefore, it is only possible to multiply m x n and n x p matrices

                                           A            B
                                      | a     b |   | e    f |           | ae + bg      af + bh |             
                                AB =  | c     d |   | g    h |        =  | ce + dg      cf + dh |
                                         
                                        
                                         
                                         
                        | Row 1 of A * column 1 of B        Row 1 of A * column 2 of B |
                        | Row 2 of A * column 1 of B        Row 2 of A * column 2 of B |

                         """)



                print("""



                                              **** HERES AN EXAMPLE ****
                    To multiply a matrix by another matrix we need to do the "dot product" of rows and columns
                         The "Dot Product" is where we multiply matching members, then sum up:
    
        
                                          | 1      2       3|       | 7     8|
                                          | 4      5       6|       | 9    10|
                                                                    | 11   12|
    
    
               1st row and 1st column:      (1, 2, 3) • (7, 9, 11) = 1×7 + 2×9 + 3×11    = 58
               
                We match the 1st members (1 and 7), multiply them, likewise for the 2nd members (2 and 9)
                 and the 3rd members (3 and 11), and finally sum them up.
               
               1st row and 2nd column:      (1, 2, 3) • (8, 10, 12) = 1×8 + 2×10 + 3×12  = 64
               2nd row and 1st column:      (4, 5, 6) • (7, 9, 11) = 4×7 + 5×9 + 6×11    = 139
               2nd row and 2nd column:      (4, 5, 6) • (8, 10, 12) = 4×8 + 5×10 + 6×12  = 154




                From this we get:
                                         | 1      2       3|       | 7     8|
                                         | 4      5       6|   x   | 9    10|      =        | 58      64 |  
                                                                   | 11   12|               | 139    154 |




                             GREAT NOW THAT YOU KNOW THE RULES RETURN TO THE MENU TO PLAY

                 """)

            if choice == "4":
                os.system('cls')
                print("""                               Game of Gaussian Elimination
                                                                ****RULES****

                      Gaussian elimination is a method where we translate our equations into a matrix and use the matrix
                       to solve the system (i.e. find the solutions for each variable that make all the equations true). 



                        Just like starting a card game by shuffling and dealing, the start of our game of Gaussian Elimination 
                        begins by translating our equations into a matrix.
                        Here’s the system we are going to solve:    y + 2z = -4
                                                                x + 2y - z =  6
                                                                    2y + z =  1
                                                                    
                                                                                                                                        
                        """)

                os.system('cls')
                print("""
                                             **** HERE'S AN EXAMPLE ****

                                      A        +         B     
                                |  2    -3 |       |  9     -5 |          | 11     -8 |
                                |  1     0 |   +   |  0     13 |     =    |  1     13 |
                                | -1     3 |       | -1      3 |          | -2      6 |



                            GREAT NOW THAT YOU KNOW THE RULES RETURN TO THE MENU TO PLAY

                """)



main()


