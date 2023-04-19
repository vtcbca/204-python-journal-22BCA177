#python script to check string is palindrome or not
Y=input("Enter string :")
s=Y[::-1]
if(Y==s):
    print("String  is palindrome !")
else:
    print("String is not palindrome !")
