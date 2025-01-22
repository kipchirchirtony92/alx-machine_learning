#!/usr/bin/env python3
matrix = [
     [1,2,9,4,5],
     [3,8,7,3,2],
     [6,5,4,6,0]]


the_middle = [row[2:4] for row in matrix]
print("the middle row of the matrix is {}".format(the_middle))

 
