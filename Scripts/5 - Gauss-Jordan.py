from Matrix import *

'''def L(a):
    l = a
    for i in range(1, len(a)):
        for j in range(len(a[0])):
            l[i][j] = a[i][j] -
'''

if __name__ == '__main__':
    mat = Matrix([[ 3,  1, -1,  2],
                  [-5,  1,  3, -4],
                  [ 2,  0,  1, -1],
                  [ 1, -5,  3, -3]])
    res = mat.gauss()
    print(res)
