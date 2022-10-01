# Python classes 

class Person:
    def __init__(self,name,age,gender) -> None:
        self.name=name
        self.age=age
        self.gender=gender

p1= Person("Ram",22,"male")
p2=Person("Sita",20,"female")

print(f"{p1.name} is {p1.age} years old and gender is {p1.gender} ")
print(f"{p2.name} is {p2.age} years old and gender is {p2.gender} ")