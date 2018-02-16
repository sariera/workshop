# allowed papers: 100, 50, 10, 5, and rest of request

balance = 500
def withdraw(balance, request):
    print "Your Balance is: " + str(balance)
    fact = [100, 50, 10, 5, 2]
    i = 0
    if   request > balance:
        print("Can't give you all this money !!")

    elif request <= 0:
        print("More than zero plz!")
    elif request <= balance:
        balance -= request
        while request > 0 and i<= len(fact):
            if request//fact[i] != 0:
                print "Give " + str(request//fact[i]) + " of " + str(fact[i])
                request -= (request//fact[i] * fact[i])
                i += 1
            else:
                i += 1
    return balance

balance = 500

balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)
        
            
        
