from datetime import date
from datetime import datetime
import Book
import Bill


#definingempty dictionary and list
bookDictionary = {}
borrowedBooks = []
borrowedID = []

#Creating borrowBook Function 
def borrowBook():
    sum = 0
    bookIDList = []
    #checking user input
    for each in bookDictionary:
        bookIDList.append(each)
    bookID = int(input("Enter book id to borrow book: "))

    if bookID not in bookIDList:
        print("\n" + "++" * 30 + "\n")
        print("Please provide a valid Book ID !!!".center(50) + "\n" + "++" * 30 + "\n")
        borrowBook()

    if bookID in bookIDList:
        
        borrowedBooks.append(bookDictionary[bookID][0])
        borrowedID.append(bookID)
        quantity = bookDictionary[bookID][2]
        if quantity == 0:
            print("\n" + "++" * 30 + "\n" + "Book is not available!!!".center(50) + "\n" + "++" * 30 + "\n")
            from main import main

        else:
            print("\n" + "++" * 30 + "\n" + "Book is available!!!".center(50) + "\n" + "++" * 30 + "\n")
            
            f_name = input("Enter the Name of person who borrowed book: ")
            price = bookDictionary[bookID][3]
            print("The price of book is: ",price)
            
            #adding date and time
            today = date.today()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            print("Today's date and Time: ", today,current_time, "\n")

            #writing in file 
            bookDictionary[bookID][2]-= 1

            with open('books.txt', 'w') as f:
                for i in range(1, 6):
                    f.write(str(i))
                    f.write(",")
                    for j in range(4):
                        if(j == 3):
                            
                            f.write(str(bookDictionary[i][j]))
                        else:
                            f.write(str(bookDictionary[i][j]))
                        f.write(", ")
                    f.write("\n")


            print("List after a Borrow: ")
            Book.Book()
            print("Has This Person Borrowed Another Book?")
            AnotherBook = input("If yes then type Y ,if not they type n: ")
            if AnotherBook.lower() == "y":
                Book.moreBooks()
            
                
            for x in(borrowedID):
                p = bookDictionary[x][3]
                price = p[1:]
                sum = sum + float(price)
            #printing bill
            Bill.Bill(f_name,sum,today,current_time)
            
           
            


