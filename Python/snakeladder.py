from PIL import Image  #importing the image library\
import random
end=100

def show_board():
    
    #viewing the image of board
    
    img= Image.open("snake.webp")
    img.show()
    


def reached_end(points):
    
    
    if points==end:
        return True
    else:
        return False
    
def play():
    
    #input players name
    
    p1_name=input("Player 1 please enter your name")
    p2_name=input("Player 2 please enter your name")
    #initial points of player 1
    pp1=0
    #initial points of player 2
    pp2=0

    turn=0

    while(1):
        if turn%2==0:
            #player 1 turn
            print(p1_name,"Your turn")
            # askl the choice
            c=input("Press 1 tocontinue or 0 to Quit")
            if c==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print("Quiting the game , Thanks for playing")
                break
            # Generate a random number from 1,2,3,4,5,6
            dice=random.randint(1,6)
            print("Dice Showed :",dice)
            # add the point
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            # check if the player goes beyond the board.
            if pp1>end:
                pp1=end
            print(p1_name,"YOur score :",pp1)

            if reached_end(pp1):
                print(p1_name,"Won")
                break
        else:
            #Player 2 turn:========
            print(p2_name,"Your turn")
            # askl the choice
            c=input("Press 1 tocontinue or 0 to Quit")
            if c==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print("Quiting the game , Thanks for playing")
                break
            # Generate a random number from 1,2,3,4,5,6
            dice=random.randint(1,6)
            print("Dice Showed :",dice)
            # add the point
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            # check if the player goes beyond the board.
            if pp2>end:
                pp2=end
            print(p2_name,"YOur score :",pp2)

            if reached_end(pp2):
                print(p2_name,"Won")
                break  

        turn=turn+1 
def check_ladder(points):
    
    if points==8:
        print("Ladder")
        return 26
    elif points ==21:
        print('Ladder')
        return 82
    elif points ==43:
        print('Ladder')
        return 77
    elif points ==50    :
        print('Ladder')
        return 91
    elif points ==54:
        print('Ladder')
        return 93
    elif points ==62:
        print('Ladder')
        return 96
    elif points ==66:
        print('Ladder')
        return 87
    elif points ==80:
        print('Ladder')
        return 100
    else:
        #Not a ladder
        return points
    
    
def check_snake(points):
    
    if points==44:
        print('snake')
        return 22
    elif points==46:
        print('Snake')
        return 5
    elif points==48:
        print('Snake')
        return 9
    elif points==52:
        print('Snake')
        return 11
    elif points==55:
        print('Snake')
        return 7
    elif points==59:
        print('Snake')
        return 17
    elif points==64:
        print('Snake')
        return 36
    elif points==69:
        print('Snake')
        return 33
    elif points==73:
        print('Snake')
        return 1
    elif points==83:
        print('Snake')
        return 19
    elif points==92:
        print('Snake')
        return 51
    elif points==95:
        print('Snake')
        return 24
    elif points==98:
        print('Snake')
        return 28
    else:
        # NOt SNAKE
        return points
    



show_board()
play()