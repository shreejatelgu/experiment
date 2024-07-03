#simple pyramind 
n=5
for i in range(1,n+1):
    print('*'*i)

#inverted pattern 
n=5 
for i in range(n,0,-1):
    print('*'*i)

#right allined riangle
b=5 
for i in range(1,n+1):
    print(' '*(b-i)+'*'*i)

#pyramind pattern

c=5
for i in range(1,n+1): 
    print(' '*(c-i)+'*'*(2*i-1))

#inverted pattern
d=5 
for i in range(n,0,-1):
    print(' '*(d-i)+'*'*(2*i-1))


#diamond pattern
d=5 
for i in range(n,0,-1):
    print(' '*(d-i)+'*'*(2*i-1))
for i in range (n-1,0,-1):
    print()


#floyids triangle 
n = 5 
num = 1 
for i in range (1,n+1):
    for j in range (1,i+1):
        print (num,end='')
    num+=1 
    print()

import  shree 

print(shree)