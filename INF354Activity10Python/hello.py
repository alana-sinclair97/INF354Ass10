import random
#def functionPrime():
 #   p = 0
  #  studentNo =16255977
   # for i < studentNo 
    #    bool isPrime = True

# number 1
studentNo = "16255977"
msg = "0. The student number is: "
p = 0
print(msg, studentNo)

for c in (studentNo):
    #print(c)
    b = int(c)
    if (b == 2 or b == 3 or b == 5 or b == 7):
        p = p + 1
        if (p == 0):
            p=p+1
        #print(p)
        

msg = "1. The number of prime numbers in this student number is: "
print(msg + str(p))


#number 2
for x in range(1):
    msg = "2. The random number is: "
    q = (random.randint(25,50))
    print(msg + str(q))



#number 3
msg = "3. The number of strings to be generated is: "
r=0
r = int(q)%int(p)
print(msg+ str(r))


#number 4
from random import choice
from string import ascii_lowercase
list=[]
for x in range(r):

    if((int(x) % int(2)) ==0):
        l=5
    else:
        l=7
    
    list.append((str(x)+ '-'+' '.join(choice(ascii_lowercase) for i in range(l))))
    
    for w in list:
        print(w)



listVowels=[]
litt=[]
vowels=0
i=0
b=int(0)
for i in list:
    litt.append(i)
    tmp=i
    for y in tmp:
        b = y
        
        if(b=='a' or b=='e' or b=='o' or b=='u'):
            vowels+=1
    
    print(vowels)
    vowels=0