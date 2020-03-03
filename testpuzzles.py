def getinputgrid(level):
    if level == 1:
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
    if level == 2:
        # Harder Game
        inputgrid = [[0,7,0,0,8,0,0,0,0],
                    [0,0,5,9,0,0,0,3,1],
                    [0,0,1,0,0,0,2,0,0],
                    [0,4,0,2,0,0,8,5,0],
                    [0,0,0,4,0,7,0,0,0],
                    [0,1,7,0,0,8,0,2,0],
                    [0,0,9,0,0,0,6,0,0],
                    [1,6,0,0,0,3,5,0,0],
                    [0,0,0,0,7,0,0,8,0]]

    if level == 3:
        # Extreme Game
        inputgrid = [[0,4,7,0,0,0,9,0,1],
                    [0,0,0,0,0,0,0,0,8],
                    [0,6,0,0,0,0,0,0,5],
                    [0,5,0,7,3,4,0,2,0],
                    [0,0,0,6,8,0,4,0,0],
                    [0,0,0,2,0,0,0,0,0],
                    [4,3,0,0,0,1,0,6,0],
                    [0,0,0,0,7,0,0,0,9],
                    [0,0,1,0,0,0,0,0,0]]
    if level ==99:
        # Extreme Game
        inputgrid = [[],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    []]
    return inputgrid