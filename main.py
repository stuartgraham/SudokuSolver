from pprint import pprint as pprint

def solver(inputgrid, answergrid):
    rowcount = 0
    for row in inputgrid:
        colcount = 0
        for col in row:
            # Only deal with blanks (0's)
            if col == 0:
                # First solver - get rid of answers in the row
                pass
                for range (1,9):
                    answergrid[rowcount][colcount]
                    inputgrid[rowcount]
            else:
                # Clear answer array if answer there
                print(str(rowcount) + ',' + str(colcount))
                answergrid[rowcount][colcount] = []

            print('#'*20)
            print('Cell value: ' + str(col))
            print('Answer grid : ' + str(rowcount) + ',' + str(colcount))
            print(answergrid[rowcount][colcount])

            
            colcount +=1
        rowcount +=1 


    return inputgrid, answergrid


inputgrid = [[0,7,0,0,8,0,0,0,0],
              [0,0,5,9,0,0,0,3,1],
              [0,0,1,0,0,0,2,0,0],
              [0,4,0,2,0,0,8,5,0],
              [0,0,0,4,0,7,0,0,0],
              [0,1,7,0,0,8,0,2,0],
              [0,0,9,0,0,0,6,0,0],
              [1,6,0,0,0,3,5,0,0],
              [0,0,0,0,7,0,0,8,0]]

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
solvedgrid = solver(inputgrid, answergrid)
while solveattempt < 10:
    solvedgrid = solver(solvedgrid[0], solvedgrid[1])
    print('#'*40)
    print('#'*40)
    #pprint(solvedgrid[1])
    print('#'*40)
    displaygrid(solvedgrid[0])
    solveattempt += 1