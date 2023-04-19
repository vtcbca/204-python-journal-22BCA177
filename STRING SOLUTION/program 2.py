#write a script to enter any sentence and print those word which is palindrome also print total number of palindrome word.
input("Enter sentece:")
s=sr.split(" ")
X=0
Y=[]
for i in s:
    if (i==i[::-1]):
        X=X+1
        Y.append(i)
if a>0:
    print('number of palindrome word in sentence is {} and palindrome words are:{}.'.format(a,d))              
else:
    print(" no palindrome word in sentence!!!")    

   