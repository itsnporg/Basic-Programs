
def draw_board(p1, p2):
    print("---------------")
    for row in range(len(p1)):
        for col in range(len(p1[0])):
            if p1[row][col] == 1:
                print("| X", end=' |')
            elif p2[row][col] == 1:
                print("| O", end=' |')
            else:
                print("   ", end='  ')
        print("\n---------------")


def is_won(p): #function to check for the winner
    # check row
    for row in p:
        if row[0] == 1 and row[1] == 1 and row[2] == 1:
            return True

    # check column
    p_transpose = [[row[i] for row in p] for i in range(len(p[0]))]
    for row in p_transpose:
        if row[0] == 1 and row[1] == 1 and row[2] == 1:
            return True

    # check diagonals
    if (p[0][0] == 1 and p[1][1] == 1 and p[2][2] == 1) or \
            (p[0][2] == 1 and p[1][1] == 1 and p[2][0] == 1):
        return True

    return False


def is_a_draw(board):   #fucntion to check if it is a draw
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True


playAgain = 'y'
while playAgain.lower() == 'y':  # you can make it one board(list) for both players, player x is 1 and player o is 2.
    p1 = [[0, 0, 0],  # X
          [0, 0, 0],
          [0, 0, 0]]
    p2 = [[0, 0, 0],  # O
          [0, 0, 0],
          [0, 0, 0]]

    board = [[0, 0, 0],  # used to detect a draw
             [0, 0, 0],
             [0, 0, 0]]
    draw_board(p1, p2)
    turn = 'x'
    while not is_won(p1) and not is_won(p2) and not is_a_draw(board): #continuing the game if no one wins and draw
        if turn == 'x':
            #taking valid input from the user
            x = int(input("Enter a row (0, 1, or 2) for player X: "))
            y = int(input("Enter a column (0, 1, or 2) for player X: "))
            while x>2 or y>2:
                print("Please enter a valid row and column values")
                x = int(input("Enter a row (0, 1, or 2) for player X: "))
                y = int(input("Enter a column (0, 1, or 2) for player X: "))
            

            p1[x][y] = 1
            board[x][y] = 1
            draw_board(p1, p2)
            if is_won(p1):
                print("X player won")
                break
            turn = 'o'

        elif turn == 'o':
            x = int(input("Enter a row (0, 1, or 2) for player O: "))
            y = int(input("Enter a column (0, 1, or 2) for player O: "))

            while x>2 or y>2:
                print("Please enter a valid row and column values")
                x = int(input("Enter a row (0, 1, or 2) for player X: "))
                y = int(input("Enter a column (0, 1, or 2) for player X: "))
            

            p2[x][y] = 1
            board[x][y] = 1
            draw_board(p1, p2)
            if is_won(p2):
                print("0 Player won")
                break
            turn = 'x'

        if is_a_draw(board):
            print("Draw")

    playAgain = input("Do you want to play again? y or n ") #checking condition for playing again
