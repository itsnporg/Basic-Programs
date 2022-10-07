
class Account:   #creation of the class Account for handeling the various operation related to the Account
    def __init__(self, id=0, balance=500.00, annualIntersetRate=0): #Constructor which assign an initial balance of $500.00
        self.__id = id
        self.__balance = balance
        self.__annualIntersetRate = annualIntersetRate

    #accessors for accessing the various values of t
    def getId(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance
    
    def getAnnualIntersetRate(self):
        return self.__annualIntersetRate
    #mutators
    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualIntersetRate(self, annualIntersetRate):
        self.__annualIntersetRate = annualIntersetRate

    def getMonthlyInterestRate(self):
        return (self.__annualIntersetRate / 12) / 100

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def deposit(self, balance): # method for handeling the deposit operation
        self.__balance += balance

    def withdraw(self, amount): #method for handeling the withdraw operation
        if self.__balance-amount>=0:
            self.__balance -= amount
        else:
            print('Withdrawal Not possible, Low Balance.')


def main():
    accounts = []

    for i in range(10): #creating 10 coounts with ID from 0 to 9
        ac = Account(i)
        accounts.append(ac)
    id=99999999999999999
    
    while (True): #infinte loop for handeling the ID verification
        id = eval(input("Enter an account id: "))
        if 0 <= id <= 9:
            while True:
                # Main Menu operations 
                print("Main menu")
                print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
                #taking choice input and performing the operation based on the given user choice
                choice = int(input(""))
                if choice == 1:
                    print("The balance is", accounts[id].getBalance(),"\n")
                elif choice == 2:
                    amount = eval(input("Enter an amount to withdraw: \n"))
                    accounts[id].withdraw(amount)
                elif choice == 3:
                    amount = eval(input("Enter an amount to deposit: \n"))
                    accounts[id].deposit(amount)
                elif choice == 4:
                    break
                else:
                    print("Invalid Input, Please Enter Correct Choice.")
        else:
            print('Invalid Input')
            pass

main()
