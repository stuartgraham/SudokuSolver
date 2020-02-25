
import re
from collections import Counter

print('Enter known values row by row')
print('Use # to denote missing squares')
print('e.g. 1#24#59##')

def get_grid():
    inputrow = 0
    inputarray = []
    while inputrow < 9:
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

def gridshuffle(grid)
    horzgrid = grid
    # creat vertgrid
    vertgrid = [] 
    for i in range(9):
        gridcol = ''
        for gridrow in grid:
            gridcol += gridrow[i]
        vertgrid.append(gridcol)
    return horzgrid, vertgrid

def solver(grid):
    grids = gridshuffle(grid)
    for gridrow in grids[0]:
        for char in gridrow:
            if char == '#':
                for i in range (1,9):
                    checkcandiate viability


#inputarray = get_grid()

#inputarray = ['#7##8####', '##59###31', '##1###2##', '#4#2##85#', '###4#7###', '#17##8#2#', '##9###6##', '16###35##', '####7##8#']
inputarray = ['#7##8####', '##59###31', '##1###2##', '#4#2##85#', '###4#7###', '#17##8#2#', '##9###6##', '16###35##', '####7##8#']

gridattempt = validategrid(inputarray)
print('Validated Grid : ' + str(gridattempt))

displaygrid(inputarray)

solver(inputarray)
