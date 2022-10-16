import borrow

#Creating Book function
def Book():
    print("---" * 35)
    print("Book ID".ljust(17), "Book-Name".ljust(30)  + "Author".ljust(20) + "Quantity".ljust(17) + "Price".ljust(15))
    print("---" * 35)

    #Opening and reading txt file
    file = open('books.txt', 'r')
    content = file.readlines()
    def splitLines():
        for each in content:
            splitList = each.split(',')
            bookID = splitList[0]
            title = splitList[1].ljust(25)
            if len(title) > 25:
                title = title[0:22].ljust(25, '.')
            author = splitList[2].ljust(25)
            quantity = splitList[3].ljust(15)
            price = splitList[4].ljust(15)

            print(bookID.ljust(15) + title + " " * 5 + author + quantity + price)
            borrow.bookDictionary[int(splitList[0])] = [splitList[1].strip(), splitList[2].strip(), int(splitList[3].strip()), splitList[4].strip()]
        print("\n",borrow.bookDictionary)
        print("\n")
    splitLines()
    file.close()

#Creating moreBooks functon
def moreBooks():   
    
    bookIDList = []
    for each in borrow.bookDictionary:
        bookIDList.append(each)
    bookID = int(input("Enter another borrowed book: "))

    if bookID not in bookIDList:
        print("\n" + "++" * 30 + "\n")
        print("Please provide a valid Book ID !!!".center(50) + "\n" + "++" * 30 + "\n")
        moreBooks(sum)

    borrow.borrowedID.append(bookID)
    borrow.borrowedBooks.append(borrow.bookDictionary[bookID][0])
    price2 = borrow.bookDictionary[bookID][3]
    print("The price of book is: ",price2 + "\n")
    print("Has This Person Borrowed Another Book?")
    AnotherBook = input("If yes then type Y ,if not they type n: " )
    if AnotherBook.lower() == "y":
        moreBooks()
    else:
        return


