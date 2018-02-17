class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        print "Welcome To " + self.bank_name
        print "Current Balance is: " + str(self.balance)
        print "#" * 34
        units = [100, 50, 10, 5, 4, 3, 2, 1]
        i = 0
        if   request > self.balance:
            print("Can't give you all this money !!")

        elif request <= 0:
            print("More than zero plz!")
        elif request <= self.balance:
            self.balance -= request
            while request > 0 and i<= len(units):
                if request//units[i] != 0:
                    print "Give " + str(request//units[i]) + " of " + str(units[i])
                    request -= (request//units[i] * units[i])
                    i += 1
                else:
                    i += 1
        print "#" * 34
        return self.balance


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
        
            
        
