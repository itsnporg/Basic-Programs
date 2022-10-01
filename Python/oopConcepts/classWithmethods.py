# We can create class with methods/ functions 


class City:
    def __init__(self,name) -> None:
        self.name=name

    def About(self):   #function class are known as methods 
        print(f"The name of city is {self.name}")

city1 = City("Kathmandu")  #creating object called city1

city1.About() #we can call the function using object

    