
import re
from collections import Counter

print('Enter known values row by row')
print('Use # to denote missing squares')
print('e.g. 1#24#59##')

def get_grid():
    rowcount = 0
    rowarray = []
    inputarray = []
    while rowcount < 9:
        inputline = ''
        inputline = input('Row : ')
        
        inputarray.append(inputline)

        inputrow += 1
    return inputarray

def validategrid(grid):
    # check 9 elements
    if len(grid) != 9:
        return False
    
    # check gridrow is 9 long
    for gridrow in grid:
        if len(gridrow) != 9:
            return False

    # check gridrow is # or 1-9
    for gridrow in grid:
        validrow = bool(re.match('^[#1-9]+$', gridrow))
        if not validrow:
            return False

    # check gridrow for duplicates
    for gridrow in grid:
        gridrow = gridrow.replace('#', '')
        if not len(set(gridrow)) == len(gridrow):
            return False

    # check vertical rows for duplicate
    for i in range(9):
        gridcol = ''
        for gridrow in grid:
            gridcol += gridrow[i]
        gridcol = gridcol.replace('#', '')
        if not len(set(gridcol)) == len(gridcol):
            return False
    
    #grid valid
    return True

def displaygrid(grid):
    rowcount = 0
    for gridrow in grid:
        charcount = 0
        rowcontent = ''
        if rowcount == 3 or rowcount == 6:
            print('━'*40)
        for char in gridrow:
            if charcount == 2 or charcount == 5:
                rowcontent += (char + ' ┃┃ ')
                #rowcontent += ( ' | ' + char + ' ┃ ')
            elif charcount == 0:
                rowcontent += (' | '  + char + ' | ')
            else:
                rowcontent += (char + ' | ')
            charcount += 1
        print(rowcontent)
        rowcount += 1

def gridshuffle(grid):
    horzgrid = grid
    # creat vertgrid
    vertgrid = [] 
    for i in range(9):
        gridcol = ''
        for gridrow in grid:
            gridcol += gridrow[i]
        vertgrid.append(gridcol)
    return horzgrid, vertgrid

def hsolver(grid):
    for gridrow in grid:
        for char in gridrow:
            if char == '#':
                for i in range (1,9):
                    continue
                    #checkcandiate viability
    return grid

def vsolver(grid):
    return grid

def solver(grid):
    #try Horziontal solver
    workinggrid = hsolver(grid)

    #get vertical grid
    workinggrids = gridshuffle(workinggrid)
    
    #try Vertical solver
    workinggrid = vsolver(workinggrids[1])
    workinggrids = gridshuffle(workinggrid)
    workinggrid = workinggrids[1]
    return workinggrid
    

#inputarray = get_grid()
#inputarray = ['#7##8####', '##59###31', '##1###2##', '#4#2##85#', '###4#7###', '#17##8#2#', '##9###6##', '16###35##', '####7##8#']
#inputarray = ['#7##8####', '##59###31', '##1###2##', '#4#2##85#', '###4#7###', '#17##8#2#', '##9###6##', '16###35##', '####7##8#']
inputarray = [[0,7,0,0,8,0,0,0,0],
              [0,0,5,9,0,0,0,3,1],
              [0,0,1,0,0,0,2,0,0],
              [0,4,0,2,0,0,8,5,0],
              [0,0,0,4,0,7,0,0,0],
              [0,1,7,0,0,8,0,2,0],
              [0,0,9,0,0,0,6,0,0],
              [1,6,0,0,0,3,5,0,0],
              [0,0,0,0,7,0,0,8,0]]

#gridattempt = validategrid(inputarray)
print('Validated Grid : ' + str(gridattempt))

solveattempt = 0
while solveattempt < 10:
    solvedgrid = solver(inputarray)
    print('#'*40)
    print('#'*40)
    displaygrid(solvedgrid)
    solveattempt += 1