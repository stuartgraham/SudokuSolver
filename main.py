from pprint import pprint as pprint
import time
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


def solver(inputgrid, answergrid, firstrun=False):
    rowcount = 0
    for row in inputgrid:
        colcount = 0
        for col in row:
            # Only deal with blanks (0's)
            if col == 0:
                # First solver - get rid of answers in the row
                for i in range(1,10):
                    if i in inputgrid[rowcount]:
                        try:
                            answergrid[rowcount][colcount].remove(i)
                        except:
                            continue

                # Dedupe answer grid based on mini grid             
                minisquare = minisquared(str(rowcount) + ',' + str(colcount))
                for coord in minisquare:
                    coord = coord.split(',')
                    rowcoord, colcoord = int(coord[0]), int(coord[1])
                    if inputgrid[rowcoord][colcoord] in range (1,10):
                        try:
                            answergrid[rowcount][colcount].remove(inputgrid[rowcoord][colcoord])
                        except:
                            continue
                
                # Dedupe answer grid, if unique answer
                if not firstrun:
                    temprowcount = [item for items in answergrid[rowcount] for item in items]
                    for answers in answergrid[rowcount]:
                        answerindex = answergrid[rowcount].index(answers)
                        for answer in answers:
                            answercount = temprowcount.count(answer)
                            if answercount == 1:
                                print('Found a unique answer : ' + str(answer) + ' at answer index ' + str(answerindex))
                                print(answergrid[rowcount])
                                time.sleep(0.5)
                            

            else:
                # Clear answer array if answer there
                answergrid[rowcount][colcount] = []

            #print('#'*20)
            #print('Cell value: ' + str(col))
            #print('Answer grid : ' + str(rowcount) + ',' + str(colcount))
            #print(answergrid[rowcount][colcount])
            
            # Change value if answers down to 1 possible
            if len(answergrid[rowcount][colcount]) == 1:
                print ('#'*40)
                print ('!! Changing : Co-ord ' + str(rowcount) + ',' + str(colcount) + ' to ' + str(answergrid[rowcount][colcount][0]) + ' !!' )
                print ('#'*40)
                inputgrid[rowcount][colcount] = answergrid[rowcount][colcount][0]
                time.sleep(1)
                
            colcount +=1
        rowcount +=1 
    return inputgrid, answergrid

def minisquared(inputstring):
    minisquare = [["0,0","0,1","0,2","1,0","1,1","1,2","2,0","2,1","2,2"],
              ["0,3","0,4","0,5","1,3","1,4","1,5","2,3","2,4","2,5"],
              ["0,6","0,7","0,8","1,6","1,7","1,8","2,6","2,7","2,8"],
              ["3,0","3,1","3,2","4,0","4,1","4,2","5,0","5,1","5,2"],
              ["3,3","3,4","3,5","4,3","4,4","4,5","5,3","5,4","5,5"],
              ["3,6","3,7","3,8","4,6","4,7","4,8","5,6","5,7","5,8"],
              ["6,0","6,1","6,2","7,0","7,1","7,2","8,0","8,1","8,2"],
              ["6,3","6,4","6,5","7,3","7,4","7,5","8,3","8,4","8,5"],
              ["6,6","6,7","6,8","7,6","7,7","7,8","8,6","8,7","8,8"]]
    for sub_i, sublist in enumerate(minisquare):
        try:
            x = sub_i, sublist.index(inputstring)
        except ValueError:
            pass
    
    return minisquare[x[0]]
     

def gridrotator(inputgrid):
    tempinputgrid = []
    for i in range(9):
        tempinputrow=[]
        for row in inputgrid:
            tempinputrow.append(row[i])
        tempinputgrid.append(tempinputrow)
    grid = tempinputgrid
    return grid

# Harder Game
#inputgrid = [[0,7,0,0,8,0,0,0,0],
#              [0,0,5,9,0,0,0,3,1],
#              [0,0,1,0,0,0,2,0,0],
#              [0,4,0,2,0,0,8,5,0],
#              [0,0,0,4,0,7,0,0,0],
#              [0,1,7,0,0,8,0,2,0],
#              [0,0,9,0,0,0,6,0,0],
#              [1,6,0,0,0,3,5,0,0],
#              [0,0,0,0,7,0,0,8,0]]

# Easier Game
inputgrid = [[0,4,0,0,0,6,0,0,0],
              [1,0,0,0,0,0,0,9,0],
              [0,7,8,9,0,5,0,0,1],
              [0,0,0,0,0,0,0,6,9],
              [0,0,2,3,0,1,5,0,0],
              [5,3,0,0,0,0,0,0,0],
              [7,0,0,8,0,2,6,4,0],
              [0,1,0,0,0,0,0,0,5],
              [0,0,0,6,0,0,0,1,0]]


        

# Initialise answergrid
def init_answergrid(inputgrid):
    answergrid = []
    for row in inputgrid:
        answerrow = []
        for col in row:
            possibleanswer = [1,2,3,4,5,6,7,8,9]
            if col in possibleanswer:
                possibleanswer.remove(col)
            answerrow.append(possibleanswer)
        answergrid.append(answerrow) 
    return answergrid

def displaygrid(grid):
    rowcount = 0
    for row in grid:
        if rowcount == 3 or rowcount == 6:
            print('━'*40)
        colcount = 0
        rowcontent = ''
        for col in row:
            if colcount == 2 or colcount == 5:
                rowcontent += (str(col) + ' ┃┃ ')
            elif colcount == 0:
                rowcontent += (' | '  + str(col) + ' | ')
            else:
                rowcontent += (str(col) + ' | ')
            colcount += 1
        print(rowcontent)
        rowcount += 1

answergrid = init_answergrid(inputgrid)
#pprint(answergrid)
displaygrid(inputgrid)

solveattempt = 0
solvedgrid = solver(inputgrid, answergrid, True)
while solveattempt < 50:
    rotatedgrid = []
    solvedgrid = solver(solvedgrid[0], solvedgrid[1])
    rotatedgrid.append(gridrotator(solvedgrid[0]))
    rotatedgrid.append(gridrotator(solvedgrid[1]))
    solvedgrid = solver(rotatedgrid[0], rotatedgrid[1], True)
    rotatedgrid[0] = gridrotator(solvedgrid[0])
    rotatedgrid[1] = gridrotator(solvedgrid[1])
    solvedgrid = rotatedgrid[0],rotatedgrid[1]
    #print('#'*40)
    #print('#'*40)
    #pprint(solvedgrid[1])
    print('')
    print('')
    displaygrid(solvedgrid[0])
    solveattempt += 1

for row in solvedgrid[1]:
    print(str(row))