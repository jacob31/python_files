# file name: identity_matrix.py 
# by: Ben Silbernagel
# date: 5/24/2016
# class: Intro to Computer Science, by Udacity
# purpose: see comment below of project description

# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)
def is_square(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows != num_cols:
        return False
    else:
        return True

def is_identity_matrix(matrix):
    length = len(matrix)
    loop_count = length * length
    e = 0
    i = 0
    verify = False

    while is_square(matrix):
        continue
    else:
        return False

    while e < loop_count:
        while i < loop_count:
            if matrix[e][i] == 1:
                if e == i:
                    verify = True
                else:
                    return False
            elif matrix[e][i] == 0:
                if e != i:
                    verify = True
                else:
                    return False
            else:
                verify = False
            print str(matrix[e][i]) +" "+ str(e) +" "+ str(i)
            i = i + 1
        i = 0
        e = e + 1
        return verify
    return False

# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],
           [0,1,0,1],
           [0,0,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False