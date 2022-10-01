import random
print("                     $$$$$ TIC-TAC-TOE (KAT-PIT) $$$$$ \n\n\n\n") 
l1= [0, 1, 2] 
l2= [0, 1, 2] 
l3= [0, 1, 2] 
print("Here is the chart as a reference to find the place where you want to print your mark (|X or O| \n\n")
print("l1=",l1, "\nl2=",l2, "\nl3=",l3, "\n\n\n\n")
print("Choose if you want to play with computer or you guys are in pair ;)\n\n\n ")
print("Enter 1 to play with computer(Its under construction but you can try) or 2 to play in pair....")
choice=int(input("Enter your choice:::"))
# MAN VS MAN INPUT TAKING
if choice==2:
    print("Now register your names..")
    nx=input("Enter name of player X::::")
    no=input("Enter name of player O::::")
    print(nx,"VS" ,no,"\n\n\n\n\n")
    print("Let's begin ........")
    for i in range(1,6):
        print(">>>>>>>>>",nx,"'s turn \n", sep="")
        a=input("Entre list no:")
        b=int(input("Enter place:"))
        if(a=="l1"):
            l1[b]="X"
        elif(a=="l2"):
            l2[b]="X"
        elif(a=="l3"):
            l3[b]="X"
        else:
            print("Invalid list number!!!!!\n<<<You are fined by skipping your one chance!>>>")
        print(" ",l1, "\n ",l2, "\n ",l3, "\n\n\n\n")
#CASES    TO      WIN        
        if(l1[0]==l2[1] and l2[1]==l3[2]):
            if l1[0]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[0]=="O":
                print(no,"wins :-)")
                break    
        elif(l1[0]==l1[1] and l1[1]==l1[2]):
            if l1[0]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[0]=="O":
                print(no,"wins :-)")
                break    
        elif(l2[0]==l2[1] and l2[1]==l2[2]):
            if l2[0]=="X":
                print(nx,"wins :-)")
                break     
            elif l2[0]=="O":
                print(no,"wins :-)")
                break    
        elif(l3[0]==l3[1] and l3[1]==l3[2]):
            if l3[0]=="X":
                print(nx,"wins :-)")
                break     
            elif l3[0]=="O":
                print(no,"wins :-)")
                break    
        elif(l1[0]==l2[0] and l2[0]==l3[0]):
            if l1[0]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[0]=="O":
                print("O wins :-)")
                break    
        elif(l1[1]==l2[1] and l2[1]==l3[1]):
            if l1[1]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[1]=="O":
                print(no,"wins :-)")
                break    
        elif(l1[2]==l2[1] and l2[1]==l3[0]):
            if l1[2]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[2]=="O":
                print(no,"wins :-)")
                break    
        elif(l1[2]==l2[2] and l2[2]==l3[2]):
            if l1[2]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[2]=="O":
                print(no,"wins :-)")
                break
   
        print(">>>>>>>>>",no,"'s turn \n", sep="")
        a=input("Entre list no:")
        b=int(input("Enter place:"))
        if(a=="l1"):
            l1[b]="O"
        elif(a=="l2"):
            l2[b]="O"
        elif(a=="l3"):
            l3[b]="O"
        else:
            print("Invalid list number!!!!!\n<<<You are fined by skipping your one chance!>>>")
        print(" ",l1, "\n ",l2, "\n ",l3, "\n\n\n\n")
        #CASES    TO      WIN        
        if(l1[0]==l2[1] and l2[1]==l3[2]):
            if l1[0]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[0]=="O":
                print(no,"wins :-)")
                break    
        elif(l1[0]==l1[1] and l1[1]==l1[2]):
            if l1[0]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[0]=="O":
                print(no,"wins :-)")
                break    
        elif(l2[0]==l2[1] and l2[1]==l2[2]):
            if l2[0]=="X":
                print(nx,"wins :-)")
            elif l2[0]=="O":
                print(no,"wins :-)")
                break    
        elif(l3[0]==l3[1] and l3[1]==l3[2]):
            if l3[0]=="X":
                print(nx,"wins :-)")
                break     
            elif l3[0]=="O":
                print(no,"wins :-)")
                break    
        elif(l1[0]==l2[0] and l2[0]==l3[0]):
            if l1[0]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[0]=="O":
                print(no,"wins :-)")
                break    
        elif(l1[1]==l2[1] and l2[1]==l3[1]):
            if l1[1]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[1]=="O":
                print(no,"wins :-)")
                break    
        elif(l1[2]==l2[1] and l2[1]==l3[0]):
            if l1[2]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[2]=="O":
                print(no,"wins :-)")
                break    
        elif(l1[2]==l2[2] and l2[2]==l3[2]):
            if l1[2]=="X":
                print(nx,"wins :-)")
                break     
            elif l1[2]=="O":
                print(no,"wins :-)")
                break
        
    else:
        print("No Results :~(")




elif choice==1:             #TO  BE  CONSTRUCTED NICELY
    print("COMPUTER VS MAN \n\n\nGet ready  ;) \n")
    print("It is not sensitive of horizontal cases of winning so keep it in mind while playing.(We are very sorry for that but after few days you will be playing completely designed game with computer.....:)")
    print("\n\n>>>>>>>Your turn:-")
    
    for i in range(0,6):
        a=input("Entre list no:")
        b=int(input("Enter place:"))
        s=random.randint(0,2)
        if(a=="l1"):
            l1[b]="X"
            print(" ",l1, "\n ",l2, "\n ",l3, "\n\n\n\n")
            #CASES  TO  WIN
            if(l1[0]==l2[1] and l2[1]==l3[2]):
                if l1[0]=="X":
                    print("You win :-)")
                    break
                elif l1[0]=="O":
                    print("You lose:-(")
                    break               
            elif(l1[0]==l2[0] and l2[0]==l3[0]):
                if l1[0]=="X":
                    print("You win :-)")
                    break            
                elif l1[0]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[1]==l2[1] and l2[1]==l3[1]):
                if l1[1]=="X":
                    print("You win :-)")
                    break            
                elif l1[1]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[1] and l2[1]==l3[0]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[2] and l2[2]==l3[2]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break        

            print(">>>>>>>>Commputer's turn:-")
            l2[s]="O"
            print(" ",l1, "\n ",l2, "\n ",l3, "\n\n\n\n")
            #CASES  TO  WIN
            if(l1[0]==l2[1] and l2[1]==l3[2]):
                if l1[0]=="X":
                    print("You win :-)")
                    break
                elif l1[0]=="O":
                    print("You lose:-(")
                    break               
            elif(l1[0]==l2[0] and l2[0]==l3[0]):
                if l1[0]=="X":
                    print("You win :-)")
                    break            
                elif l1[0]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[1]==l2[1] and l2[1]==l3[1]):
                if l1[1]=="X":
                    print("You win :-)")
                    break            
                elif l1[1]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[1] and l2[1]==l3[0]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[2] and l2[2]==l3[2]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break    
        elif(a=="l2"):
            l2[b]="X"
            print(" ",l1, "\n ",l2, "\n ",l3, "\n\n\n\n")
            #CASES  TO  WIN
            if(l1[0]==l2[1] and l2[1]==l3[2]):
                if l1[0]=="X":
                    print("You win :-)")
                    break
                elif l1[0]=="O":
                    print("You lose:-(")
                    break               
            elif(l1[0]==l2[0] and l2[0]==l3[0]):
                if l1[0]=="X":
                    print("You win :-)")
                    break            
                elif l1[0]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[1]==l2[1] and l2[1]==l3[1]):
                if l1[1]=="X":
                    print("You win :-)")
                    break            
                elif l1[1]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[1] and l2[1]==l3[0]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[2] and l2[2]==l3[2]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break 
            print(">>>>>>>>Commputer's turn:-")
            l3[s]="O"
            print(" ",l1, "\n ",l2, "\n ",l3, "\n\n\n\n")
            #CASES  TO  WIN
            if(l1[0]==l2[1] and l2[1]==l3[2]):
                if l1[0]=="X":
                    print("You win :-)")
                    break
                elif l1[0]=="O":
                    print("You lose:-(")
                    break               
            elif(l1[0]==l2[0] and l2[0]==l3[0]):
                if l1[0]=="X":
                    print("You win :-)")
                    break            
                elif l1[0]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[1]==l2[1] and l2[1]==l3[1]):
                if l1[1]=="X":
                    print("You win :-)")
                    break            
                elif l1[1]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[1] and l2[1]==l3[0]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[2] and l2[2]==l3[2]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break 
        elif(a=="l3"):
            l3[b]="X"
            print(" ",l1, "\n ",l2, "\n ",l3, "\n\n\n\n")
            #CASES  TO  WIN
            if(l1[0]==l2[1] and l2[1]==l3[2]):
                if l1[0]=="X":
                    print("You win :-)")
                    break
                elif l1[0]=="O":
                    print("You lose:-(")
                    break               
            elif(l1[0]==l2[0] and l2[0]==l3[0]):
                if l1[0]=="X":
                    print("You win :-)")
                    break            
                elif l1[0]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[1]==l2[1] and l2[1]==l3[1]):
                if l1[1]=="X":
                    print("You win :-)")
                    break            
                elif l1[1]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[1] and l2[1]==l3[0]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[2] and l2[2]==l3[2]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break 
            print(">>>>>>>>Commputer's turn:-")
            l1[s]="O"
            print(" ",l1, "\n ",l2, "\n ",l3, "\n\n\n\n")
            #CASES  TO  WIN
            if(l1[0]==l2[1] and l2[1]==l3[2]):
                if l1[0]=="X":
                    print("You win :-)")
                    break
                elif l1[0]=="O":
                    print("You lose:-(")
                    break               
            elif(l1[0]==l2[0] and l2[0]==l3[0]):
                if l1[0]=="X":
                    print("You win :-)")
                    break            
                elif l1[0]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[1]==l2[1] and l2[1]==l3[1]):
                if l1[1]=="X":
                    print("You win :-)")
                    break            
                elif l1[1]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[1] and l2[1]==l3[0]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break        
            elif(l1[2]==l2[2] and l2[2]==l3[2]):
                if l1[2]=="X":
                    print("You win :-)")
                    break            
                elif l1[2]=="O":
                    print("You lose:-(")
                    break 
        else:
            print("Invalid list number!!!!!\n<<<You are fined by skipping your one chance!>>>")
    else:
        print("No Results:~(")
else:
    print("Invalid input!!!!!")
print("HOPE YOU LIKED THE GAME :-)\n ")
print("$$$$$$$$$$$$$$$$$ Developed by-SHIVANSH KUMAR DUBEY $$$$$$$$$$$$$$$$$")
print("Press enter key to close the game")
r=input()
print("XXXXXXXXXXXXXXX            GAME OVER               XXXXXXXXXXXXXXX")
