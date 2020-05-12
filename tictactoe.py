def printM(arr):
    print("---------")
    for i in reversed(range(3)):
        print("| " + arr[0][i] + " " + arr[1][i] + " " + arr[2][i] + " |")
    print("---------")


def checkCondition(matrix):
    """
    Checks condition of current tic tac toe matrix
    @param matrix: 2D array of X's, O's and _'s
    @return: condition in string
    """
    # check X's and O's
    x_counter = 0
    o_counter = 0
    empty_counter = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == "X":
                x_counter += 1
            elif matrix[i][j] == "O":
                o_counter += 1
            elif matrix[i][j] == "_":
                empty_counter += 1

    # calculate difference
    diff = abs(x_counter - o_counter)
    if diff < 2:
        # okay, continue
        x_wins = False
        o_wins = False
        # horizontal check
        for i in range(3):
            if matrix[i][0] == "X" and matrix[i][1] == "X" and matrix[i][2] == "X":
                x_wins = True
        for i in range(3):
            if matrix[i][0] == "O" and matrix[i][1] == "O" and matrix[i][2] == "O":
                o_wins = True
        # vertical check
        for j in range(3):
            if matrix[0][j] == "X" and matrix[1][j] == "X" and matrix[2][j] == "X":
                x_wins = True
        for j in range(3):
            if matrix[0][j] == "O" and matrix[1][j] == "O" and matrix[2][j] == "O":
                o_wins = True
        # diagonal check
        if matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X":
            x_wins = True
        if matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O":
            o_wins = True
        if matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X":
            x_wins = True
        if matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O":
            o_wins = True

        # check completed
        if (x_wins is False and o_wins is False) and empty_counter > 0:
            return "Game not finished"
        elif (x_wins is False and o_wins is False) and empty_counter == 0:
            return "Draw"
        elif x_wins is True and o_wins is False:
            return "X wins"
        elif x_wins is False and o_wins is True:
            return "O wins"
        elif x_wins is True and o_wins is True:
            return "Impossible"
    else:
        return "Impossible"


def straightInput(cross):
    return [[cross[i + 6], cross[i + 3], cross[i]] for i in range(3)]


def userInput(matrix, argument):
    possible_input = ["1", "2", "3"]
    print("Enter the coordinates: > ", end="")
    coordinates = input().split()
    # check for correct input
    for i in range(len(coordinates)):
        if not coordinates[i].isdigit():
            print("You should enter numbers!")
            return userInput(matrix, argument)
    # check if is 1 to 3
    for i in range(len(coordinates)):
        if coordinates[i] not in possible_input:
            print("Coordinates should be from 1 to 3!")
            return userInput(matrix, argument)
    # check for intersection
    if matrix[int(coordinates[0]) - 1][int(coordinates[1]) - 1] != "_":
        print("This cell is occupied! Choose another one!")
        return userInput(matrix, argument)
    matrix[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = argument
    return matrix


field = straightInput("_________")
printM(field)
while True:
    field = userInput(field, "X")
    printM(field)
    condition = checkCondition(field)
    if condition == "X wins":
        print(condition)
        break
    if condition == "O wins":
        print(condition)
        break
    if condition == "Draw":
        print(condition)
        break
    field = userInput(field, "O")
    printM(field)
    condition = checkCondition(field)
    if condition == "X wins":
        print(condition)
        break
    if condition == "O wins":
        print(condition)
        break
    if condition == "Draw":
        print(condition)
        break
