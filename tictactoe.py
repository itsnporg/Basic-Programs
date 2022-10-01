import os

os.system("cls")

player1 = input("enter first player name :")
player2 = input("enter second player name :")
print("lets start!!")
print("1.3*3  2.4*4  3.5*5")
boardno = input("choose board number :")


if boardno == "1":
 class Board():
    def __init__(self):
        self.cells =[" "," "," "," "," "," "," "," "," "," ",]
    def display(self):
        print(" %s |%s|%s" %(self.cells[1],self.cells[2],self.cells[3],))
        print("-------------")
        print(" %s |%s|%s" %(self.cells[4],self.cells[5],self.cells[6],))
        print("--------------")
        print(" %s |%s|%s" %(self.cells[7],self.cells[8],self.cells[9],))
    def update_cell(self, cell_no, player):
        if self.cells[cell_no]== " ":
         self.cells[cell_no] = player

        

    def is_winner(self,player):
        if self.cells[1] ==player and self.cells[2] ==player and self.cells[3] ==player:
            return True
        if self.cells[4] ==player and self.cells[5] ==player and self.cells[6] ==player:
            return True
        if self.cells[7] ==player and self.cells[8] ==player and self.cells[9] ==player:
            return True
        if self.cells[1] ==player and self.cells[5] ==player and self.cells[9] ==player:
            return True

        if self.cells[3] ==player and self.cells[5] ==player and self.cells[7] ==player:
            return True

        if self.cells[1] ==player and self.cells[4] ==player and self.cells[7] ==player:
            return True

        if self.cells[2] ==player and self.cells[5] ==player and self.cells[8] ==player:
            return True



    def reset(self):
        self.cells=[" "," "," "," "," "," "," "," "," "," "," "," "," "," ",]



elif boardno == "2":
 class Board():
    def __init__(self):
        self.cells =[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",]
    def display(self):
        print(" %s | %s| %s| %s" %(self.cells[1],self.cells[2],self.cells[3],self.cells[4]))
        print("-------------")
        print(" %s | %s| %s| %s" %(self.cells[5],self.cells[6],self.cells[7],self.cells[8]))
        print("--------------")
        print(" %s | %s| %s| %s" %(self.cells[9],self.cells[10],self.cells[11],self.cells[12]))
        print("--------------")
        print(" %s | %s| %s| %s" %(self.cells[13],self.cells[14],self.cells[15],self.cells[16]))
    def update_cell(self, cell_no, player):
        if self.cells[cell_no]== " ":
         self.cells[cell_no] = player
    def is_winner(self,player):
        if self.cells[1] ==player and self.cells[2] ==player and self.cells[3] ==player and self.cells[4] ==player:
            return True
        if self.cells[5] ==player and self.cells[6] ==player and self.cells[7] ==player and self.cells[8] ==player:
            return True
        if self.cells[9] ==player and self.cells[10] ==player and self.cells[11] ==player and self.cells[12] ==player:
            return True
        if self.cells[13] ==player and self.cells[14] ==player and self.cells[15] ==player and self.cells[16] ==player:
            return True
        if self.cells[4] ==player and self.cells[7] ==player and self.cells[10] ==player and self.cells[13] ==player:
            return True
        if self.cells[1] ==player and self.cells[6] ==player and self.cells[11] ==player and self.cells[16] ==player:
            return True
        if self.cells[2] ==player and self.cells[6] ==player and self.cells[10] ==player and self.cells[14] ==player:
            return True

            
    def reset(self):
        self.cells=[" "," "," "," "," "," "," "," "," "," "," "," "," "," ",]
    
elif boardno == "3":
 class Board():
    def __init__(self):
        self.cells =[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",]
    def display(self):
        print(" %s |  %s|  %s|  %s|  %s" %(self.cells[1],self.cells[2],self.cells[3],self.cells[4],self.cells[5]))
        print("------------------")
        print(" %s |  %s|  %s|  %s|  %s" %(self.cells[6],self.cells[7],self.cells[8],self.cells[9],self.cells[10]))
        print("------------------")
        print(" %s |  %s|  %s|  %s|  %s" %(self.cells[11],self.cells[12],self.cells[13],self.cells[14],self.cells[15]))
        print("------------------")
        print(" %s |  %s|  %s|  %s|  %s" %(self.cells[16],self.cells[17],self.cells[18],self.cells[19],self.cells[20]))
        print("------------------")
        print(" %s |  %s|  %s|  %s|  %s" %(self.cells[21],self.cells[22],self.cells[23],self.cells[24],self.cells[25]))
    def update_cell(self, cell_no, player):
        if self.cells[cell_no]== " ":
         self.cells[cell_no] = player
    def is_winner(self,player):
        if self.cells[1] ==player and self.cells[2] ==player and self.cells[3] ==player and self.cells[4] ==player and self.cells[5] ==player:
            return True
        if self.cells[6] ==player and self.cells[7] ==player and self.cells[8] ==player and self.cells[9] ==player and self.cells[10] ==player:
            return True
        if self.cells[11] ==player and self.cells[12] ==player and self.cells[13] ==player and self.cells[14] ==player and self.cells[15] ==player:
            return True
        if self.cells[16] ==player and self.cells[17] ==player and self.cells[18] ==player and self.cells[19] ==player and self.cells[20] ==player:
            return True
        if self.cells[21] ==player and self.cells[22] ==player and self.cells[23] ==player and self.cells[24] ==player and self.cells[25] ==player:
            return True
        if self.cells[1] ==player and self.cells[7] ==player and self.cells[13] ==player and self.cells[19] ==player and self.cells[25] ==player:
            return True
        if self.cells[5] ==player and self.cells[9] ==player and self.cells[13] ==player and self.cells[17] ==player and self.cells[21] ==player:
            return True
        if self.cells[1] ==player and self.cells[6] ==player and self.cells[11] ==player and self.cells[16] ==player and self.cells[21] ==player:
            return True
        if self.cells[2] ==player and self.cells[7] ==player and self.cells[12] ==player and self.cells[17] ==player and self.cells[22] ==player:
            return True
        if self.cells[5] ==player and self.cells[10] ==player and self.cells[15] ==player and self.cells[20] ==player and self.cells[25] ==player:
            return True
        else:
            return False
    def reset(self):
        self.cells=[" "," "," "," "," "," "," "," "," "," "," "," "," "," ",]
board = Board()

def header():
    print("welcome to this awesome game!")

# def update_cell(self, cell_no, player):
#     self.cells[cell_no] = player




def screen_refresh():
    

    header()
    board.display()


while True:
    if boardno =="1":
        screen_refresh()
        x_choice = int(input( player1 + " Please choose 1-9 "))
        # if self.cells[cell_no]== " ":
        #     print("this box is already filled by  "+player2)
        board.update_cell(x_choice, "x")
        screen_refresh()
        if board.is_winner("x"):
            screen_refresh()
            print(player1 +" wins !!")
            play_again =input("want to play  again? [y/n]")
            if play_again == "y":
                board.reset()
                continue 
            else:
                break 
        
        o_choice = int(input(player2 + " Please choose 1-9 "))

           
        board.update_cell(o_choice, "o")
        if board.is_winner("o"):
            print(player2 + " wins !!")
            play_again =input("want to play  again? [y/n]")
            if play_again == "y":
                board.reset()
                continue 
            else:
                break 

    if boardno =="2":
        screen_refresh()
        x_choice = int(input(player1 +" Please choose 1-16 "))
        if x_choice !="":
            print("this box is already filled by  "+player2)
        board.update_cell(x_choice, "x")
        screen_refresh()
        if board.is_winner("x"):
            print(player1 +" wins !!")
        play_again =input("want to play  again? [Y/N").upper
        if play_again == "Y":
            board.reset()
            continue 
        else:
            break 
       
        o_choice = int(input(player2 +" Please choose 1-16 "))
        if o_choice != " ":
            print("this box is already filled by "+player1)
        board.update_cell(o_choice, "o")
        if board.is_winner("o"):
            print(player2 +" wins !!")
            play_again =input("want to play  again? [y/n]")
            if play_again == "y":
                board.reset()
                continue 
            else:
                break 
    if boardno =="3":
        screen_refresh()
        x_choice = int(input(player1 +" Please choose 1-25 "))
        if x_choice !=" ":
            print("this box is already filled by  "+player2)
        board.update_cell(x_choice, "x")
        if board.is_winner("x"):
            print(player1 +" wins !!")
            play_again =input("want to play  again? [Y/N").upper
        if play_again == "Y":
            board.reset()
            continue 
        else:
            break 
        screen_refresh()
        o_choice = int(input(player2 +" Please choose 1-25 "))
        if o_choice != "":
            print("this box is already filled by "+player1)
        board.update_cell(o_choice, "o")
        if board.is_winner("o"):
            print(player2 + " wins !!")
            play_again =input("want to play  again? [y/n]")
            if play_again == "y":
                board.reset()
                continue 
            else:
                break 




