class customer:
    ''' this class devloped by sd and describes bank operation '''
    bank_name = 'Sd Bank'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposite(self, ammount):
        self.balance = self.balance + ammount
        print('After deposite balance is', self.balance)

    def withdrawan(self, amount):
        if amount > self.balance:
            print('Insufficient Funds cant perform this operation')
        else:
            self.balance = self.balance - amount
            print('After withdrawn balance is', self.balance)


print('Welcome to', customer.bank_name)
name = input("Enter your name")
c = customer(name)
while True:
    print("D=deposite \nW=withdrawan \ne = exit")
    option = input("Choose your Option")
    if option.lower() == 'd':
        amount = float(input("Enter amount to deposite"))
        c.deposite(amount)
    elif option.lower() == 'w':
        amount = float(input('Enter amount to withdrawan'))
        c.withdrawan(amount)
    elif option.lower() == 'e':
        print("Thanks for Banking")
        break
    else:
        print('Your option is invalid \n please valid option')
