'''
Nested loop, to be able to create and work on 2D/3D tables.

Amit : 1 2 3
Joy : 4 5 6
matrix = [[1,2,3],[4,5,6]]  (2x3)
'''

matrix = [[1,2,3],[4,5,6]]

# using nested loop access the mxtrix table
for i in matrix:
    for j in i:
        print(j,end=' ')
    print("")
