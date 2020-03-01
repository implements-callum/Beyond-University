
"""
RSA Key Generator
By Callum Clegg
Last updated: 01/03/2020
"""

import random
isValid = False

while not isValid:
    isValid = True
    P = input("Please enter a prime number: ")
    Q = input("Enter another prime number: ")

    #checks inputs are positive whole numbers.
    if not P.isnumeric() or not Q.isnumeric():
        print("P and/or Q are not positive whole numbers!")
        isValid = False
        continue
        
    P = int(P)
    Q = int(Q)

    #Checks inputs are prime.
    if P > 1 and Q > 1:
        for i in range(2, P):
            if (P % i) == 0:
                print(P, "is not a prime number.")
                isValid = False
                break
        else:
            print(P, "is a prime number.")
        
        for i in range(2, Q):
            if (Q % i) == 0:
                print(Q ,"is not a prime number.")
                isValid = False
                break 
        else:
            print(Q, "is a prime number.")
    else:
        print("One is not a prime number.")
        isValid = False
        
N = P * Q
phi_N = (P-1)*(Q-1)

#Generates co-prime integers ('e') based on 'N' & 'phi_N' (randomly selects).  
potential = list(range(2, phi_N))
results = list();
        
factors = [i for i in potential if phi_N % i == 0 or N % i == 0]

for i in potential:
    for factor in factors:
        if i % factor == 0:
            break
    else:
        results.append(i)

e = random.choice(results)
print(e);

#Generates d value(s) where d*e(mod(phi_N)) = 1 is true (randomly selects).
explore = range(1, phi_N*200)
potential = list();
potential = [i for i in explore if ((e*i) % phi_N == 1)]

d = random.choice(potential)
print(d)

universal = N
public = e
private = d

#Prints out generated keys.
print("public: ({0}, {1})".format(universal, public))
print("private: ({0}, {1})".format(universal, private))






            
        

