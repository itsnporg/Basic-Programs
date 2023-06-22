import os
square = ['0','1','2','3','4','5','6','7','8','9']

def checkwin():
    return {
        1 : square[1] == square [2] and square [2] == square [3],
        1 : square[4] == square [5] and square [5] == square [6],
        1 : square[7] == square [8] and square [8] == square [9],
        1 : square[1] == square [4] and square [4] == square [7],
        1 : square[2] == square [5] and square [5] == square [8],
        1 : square[3] == square [6] and square [6] == square [9],
        1 : square[1] == square [5] and square [5] == square [9],
        1 : square[3] == square [5] and square [5] == square [7],
        0 : (square[1] != '1' and square[2] != '2' and square[3] != '3' and square[4] != '4' and square[5] != '5' and square[6] != '6' and square[7] != '7' and square[8] != '8' and square[9] != '9')


    }.get(-1,-1)

    # if (square[1] == square [2] and square [2] == square [3]):
    #     return 1
    # elif (square[4] == square [5] and square [5] == square [6]):
    #     return 1
    # elif (square[7] == square [8] and square [8] == square [9]):
    #     return 1
    # elif (square[1] == square [4] and square [4] == square [7]):
    #     return 1
    # elif (square[2] == square [5] and square [5] == square [8]):
    #     return 1
    # elif (square[3] == square [6] and square [6] == square [9]):
    #     return 1
    # elif (square[1] == square [5] and square [5] == square [9]):
    #     return 1
    # elif (square[3] == square [5] and square [5] == square [7]):
    #     return 1
    
    # elif (square[1] != '1' and square[2] != '2' and square[3] != '3' and square[4] != '4' and square[5] != '5' and square[6] != '6' and square[7] != '7' and square[8] != '8' and square[9] != '9'):
    #     return 0
    
    # else:
    #      return -1
def board():
    print("\n\n--------\n\n")
    print("\n player 1 (X) -- player 2 (O)",end="\n")

    print ("     |     |   ",end="\n")
    print(f" {square[1]}   | {square[2]}   | {square[3]}",end= "\n")
    print ("_____|_____|_____",end="\n")
    print ("     |     |     ",end="\n")
    print(f" {square[4]}   | {square[5]}   | {square[6]}",end= "\n")
    print ("_____|_____|_____",end="\n")
    print ("     |     |     ",end="\n")
    print(f" {square[7]}   | {square[8]}   | {square[9]}",end= "\n")
    print ("     |     |   ",end="\n")
def main():
    player = 1
    i=checkwin()
    while (i == -1):
        os.system('clear')
        board()
        player = 1 if (player%2 == 1) else 2
        
        mark = 'X' if (player == 1) else 'O'
        
        choice = (int(input(f" player {player} Enter your choice :")))


        if (choice ==1 and square [1] == '1'):
            square[1] = mark    
        elif (choice ==2 and square [2] == '2'):
            square[2] = mark 
        elif (choice ==3 and square [3] == '3'):
            square[3] = mark  
        elif (choice ==4 and square [4] == '4'):
            square[4] = mark  

        elif (choice ==5 and square [5] == '5'):
            square[5] = mark  

        elif (choice ==6 and square [6] == '6'):
            square[6] = mark 
        elif (choice ==7 and square [7] == '7'):
            square[7] = mark 
        elif (choice ==8 and square [8] == '8'):
            square[8] = mark 

        elif (choice ==9 and square [9] == '9'):
            square[9] = mark 
        
        elif (choice < 1 or choice >9) :
            print ("invalid move::")
            player-= 1
        player+=1
       
        board()
        i=checkwin()
        if (i==1):
            print(f"player {player-1} with mark {mark} win")
        else:
            print("draw")  

if __name__ == '__main__':
    main()
    
