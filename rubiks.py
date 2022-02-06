from array import *
import numpy as np

# Make an n-sided cube
def populateCube(n):
    cube = np.zeros((6,n,n))
    colors = ['w', 'r', 'g', 'o', 'b', 'y']
    color = -1
    for side in range(6):
        color += 1
        for row in range(n):
            for square in range(n):
                cube[side,row,square] = color
    return(cube)

# cube: 3D array representing rubik's cube
# slice: Integer index of which cross section on the cube will be rotated
# left: The direction the cross section will rotate relative to red, the front face of the cube
# n: The size of the cube
def rotateX(cube, slice, right, n):
    if right:
        tmp = np.copy(cube[0][slice])
        for i in range(n):
            cube[0][i][slice] = cube[4][n-1-i][slice]
            cube[4][n-1-i][slice] = cube[5][slice][i]
            cube[5][n-1-slice][i] = cube[2][n-1-i][slice]
            cube[2][i][n-1-slice] = tmp[i]
    else:
        tmp = np.copy(cube[0][slice])
        for i in range(n):
            cube[0][i][slice] = cube[2][i][slice]
            cube[2][i][slice] = cube[5][n-1-slice][i]
            cube[5][n-1-slice][i] = cube[4][i][slice]
            cube[4][i][slice] = tmp[n-1-i]
    # Transpose edge if first or last slice of the cube
    if slice == 0:
        if right:
            cube[0] = np.rot90(cube[0], -1)
        else:
            cube[0] = np.rot90(cube[0], 1)
    elif slice == n - 1:
        if right:
            cube[2] = np.rot90(cube[2], -1)
        else:
            cube[2] = np.rot90(cube[2], 1)
    else:
        pass
    return cube

# cube: 3D array representing rubik's cube
# slice: Integer index of which cross section on the cube will be rotated
# down: The direction the cross section will rotate relative to red, the front face of the cube
# n: The size of the cube
def rotateY(cube, slice, down, n):
    if down:
        for i in range(n):
            tmp = cube[1][i][slice]
            cube[1][i][slice] = cube[0][n-1-i][slice]
            cube[0][n-i-1][slice] = cube[3][i][n-1-slice]
            cube[3][i][n-1-slice] = np.flip(cube[5][i][slice])
            cube[5][i][slice] = tmp
    else:
        for i in range(n):
            tmp = cube[0][i][slice]
            cube[0][i][slice] = cube[1][i][slice]
            cube[1][i][slice] = np.flip(cube[5][i][n-1-slice])
            cube[5][n-1-i][slice] = np.flip(cube[3][i][slice])
            cube[3][i][n-1-slice] = tmp
    
    # Transpose edge if first or last slice of the cube
    if slice == 0:
        if down:
            cube[4] = np.rot90(cube[4], -1)
        else:
            cube[4] = np.rot90(cube[4], 1)
    elif slice == n - 1:
        if down:
            cube[2] = np.rot90(cube[2], -1)
        else:
            cube[2] = np.rot90(cube[2], 1)
    else:
        pass
    return cube

# Like rotating U or D on a rubiks cube
#   green  red   blue    orange
#   □□□ -> □□□ -> □□□ -> □□□
#   
# White or yellow are transposed if slice is an end slice
def rotateZ(cube, slice, right, n):
    if right:
        tmp = np.copy(cube[1][slice])
        cube[1][slice] = cube[2][slice]
        cube[2][slice] = cube[3][slice]
        cube[3][slice] = cube[4][slice]
        cube[4][slice] = tmp
    else:
        tmp = np.copy(cube[1][slice])
        cube[1][slice] = cube[4][slice]
        cube[4][slice] = cube[3][slice]
        cube[3][slice] = cube[2][slice]
        cube[2][slice] = tmp

    # Transpose edge if first or last slice of the cube
    if slice == 0:
        if right:
            cube[0] = np.rot90(cube[0], -1)
        else:
            cube[0] = np.rot90(cube[0], 1)
    elif slice == n - 1:
        if right:
            cube[5] = np.rot90(cube[5], -1)
        else:
            cube[5] = np.rot90(cube[5], 1)
    else:
        pass
    return cube


def main():
    n = 3
    cube = populateCube(n)
    #cube = rotateY(cube, 0, True, n)
    print(cube)
    #cube = rotateZ(cube, 0, True, n)
    #print(cube)
    cube = rotateX(cube, 0, False, n)
    print(cube)
    

if __name__ == "__main__":
    main()