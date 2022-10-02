class person(object):
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

class gender(object):
    def __init__(self,sex) ->None:
        self.sex=sex



class programmer(person,gender):
    def __init__(self, name, age,sex,Stack,salary) -> None:
        super().__init__(name, age)
        gender.__init__(self,sex)
        self.Stack=Stack
        self.salary=salary
        
    def display(self):
        print(f"name={self.name} \n age={self.age} \n gender = {self.sex}\n stack= {self.Stack} \n salary={self.salary}")

ram = programmer("Ram",25,"male","Python",50000)
sita = programmer("Sita",21,"female","MERN",45000)

sita.display()

ram.display()


    
        
