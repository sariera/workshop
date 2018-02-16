# allowed papers: 100, 50, 10, 5, and rest of request

balance = 500
print "Your Balance is: " + str(balance)
request = int(raw_input("Enter The Requested Amount: "))
withdraw = []
fact = [100, 50, 10, 5, 2]
i = 0
if   request > balance:
    print("Can't give you all this money !!")

elif request < 0:
    print("More than zero plz!")
elif request <= balance:
    while request > 0:
        if request//fact[i] != 0:
            print "Give " + str(request//fact[i]) + " of " + str(fact[i])
            request -= (request//fact[i] * fact[i])
            i += 1
else:
    print "Your Request Not Available"
        
            
        
