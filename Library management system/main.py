import borrow
import Book
import Return
import Bill

#Defining main function
def main():
    # using while loop
    while(True):
        print("+++" * 35)
        print("Hello and Welcome to library management system".center(100))
        print("+++" * 35+ "\n\n")
        Book.Book()
        print("Enter 1 to Borrow a Book")
        print("Enter 2 to Return a book")
        print("Enter 3 to Exit")
        
        #Using try and catch for exception Handling
        try:
            userInput = int(input("Please enter a value: "))
            print()
            # Taking input from user
            if(userInput==1):
                print("You will now borrow a book")
                borrow.borrowBook()
                main()
                break
            elif(userInput==2):
                print("You will now reuturn a Book")
                Return.return_books()
            
            elif(userInput==3):
                print("---"* 30)
                print("\n Thank you for using Library management system\n".center(100))
                print("---"* 30)
                break
        except ValueError:
            print("++" *30)
            print("Invalid Input!!\n Please enter 1, 2 or 3")
            print("++" *30+ "\n\n")

# calling main function
main()

