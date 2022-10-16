from datetime import date
from datetime import datetime
import borrow
# Creating return_books function 
def return_books():
    total = 0
    bookIDList = []
    
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
   #Asking user details
    for each in borrow.bookDictionary:
        bookIDList.append(each)
    f_name = input("Name of person who returned Book: ")
    bookID = int(input("Enter book id to return book: "))

    #Checking user input
    if bookID not in bookIDList:
        print("\n" + "++" * 30 + "\n")
        print("Please provide a valid Book ID !!!".center(50) + "\n" + "++" * 30 + "\n")
        return_books()
    if bookID in bookIDList:
        quantity = borrow.bookDictionary[bookID][2]
        price = borrow.bookDictionary[bookID][3]
        book_name = borrow.bookDictionary[bookID][0]
        author_name = borrow.bookDictionary[bookID][1]

    quantity =int(quantity)+1
    total+=float(price[1:])
    print(str(total))
    # checking for fine
    print("Is the book return date expired?")
    Expire = input("Press Y for Yes and N for No: ")
    x=current_time.replace(":","")
    if(Expire.upper()=="Y"):
        day = int(input("By how many days was the book returned late?"))
        fine=3*day
        total=total+fine
    else:
        fine = 0 
    total = "{:.2f}".format(total)
    
    fileName="Return-"+f_name+str(today)+ x+".txt"
    file = open(fileName,'w')
    file.write("Return Details: \n")
    file.write("Name of Person: "+ f_name+"\n")
    file.write("Date and time of return is: "+str(today)+ " " )
    file.write(str(current_time) +"\n")
    file.write("Books Returend are: "+ borrow.bookDictionary[bookID][0]+"\n")
    file.write("Price is: " +borrow.bookDictionary[bookID][3]+ "\n")
    file.write("Fine is: "+ str(fine)+"\n")
    print("Total Bill: "+ "$"+str(total))
    file.write("Total: $"+ str(total))
    
    # Writing in file
    borrow.bookDictionary[bookID][2]+= 1
    with open('books.txt', 'w') as f:
        for i in range(1, 6):
            f.write(str(i))
            f.write(",")
            for j in range(4):
                if(j == 3):
                    f.write(str(borrow.bookDictionary[i][j]))
                else:
                    f.write(str(borrow.bookDictionary[i][j]))
                    f.write(", ")
            f.write("\n")
