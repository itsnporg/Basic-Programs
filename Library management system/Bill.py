import borrow

# creating Bill function 
def Bill(f_name,sum,today,current_time):
     print(borrow.borrowedBooks)
     sum = "{:.2f}".format(sum)
     print("\n"+"++" * 30)
     print("Customer Bill!!!".center(50)+ "\n" + "++" * 30 + "\n")
     print("Name of Customer: ",f_name)
     print("Sum is $",sum)
     print("Date and Time of Borrow is: ",today,current_time)
     print("Name of Books Borrowed: ")
     
     for i in(borrow.borrowedBooks):
         print(i)
     x=current_time.replace(":","")
     fileName = "Borrow_"+ f_name + str(today)+ x+ ".txt"
     print("++" *30 +"\n\n\n")

     file= open(fileName,'w')
     file.write("Borrow Details:"+ "\n")
     file.write("Name of Person: "+ f_name +"\n")
     file.write("Total Price of Books: "+str(sum) +"\n")
     file.write("Date and time of Borrow is: "+str(today) )
     file.write( str(current_time) +"\n")
     file.write("Books Borrowed are: "+"\n")
     
     for books in (borrow.borrowedBooks):
         file.write(books + "\n")
    
     
     file.close()
     borrow.borrowedBooks.clear()
     borrow.borrowedID.clear()
     
             
