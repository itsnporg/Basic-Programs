from bank import Bank

CHOICES = '''1.Creat New Account
2.Deposit 
3.Withdraw 
4.Balance Enquiry
5.Exit
'''


def main(usr_inp):
    try:
        while usr_inp != 5:
            if usr_inp == 1:
                acc = Bank().create_account()
                print(
                    f"account created number:{acc['number']} amount:{acc['balance']}")
            elif usr_inp == 2:
                acc_number = int(input('enter account number: '))
                deposit_amount = int(input('Enter amount to be deposited: '))
                result = Bank(acc_number).deposit(deposit_amount)
                print(result)
            elif usr_inp == 3:
                acc_number = int(input('enter account number: '))
                withdraw_amount = int(input('enter amount to withdraw: '))
                result = Bank(acc_number).withdraw(withdraw_amount)
                print(result)
            elif usr_inp == 4:
                acc_number = int(input('enter account number: '))
                result = Bank(acc_number).balance_enquiry()
                print(result)
            else:
                print('Please enter number between 1-5!')
            usr_inp = int(input(CHOICES))
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    print('***Welcome to the Bank Management system!***')
    try:
        usr_inp = int(input(CHOICES))
        main(usr_inp)
    except ValueError as err:
        print(err)
