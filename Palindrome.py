n=int(input("enter number"))
temp=0
rev=0
while(n<0):
    dig=n%10
    rev=rev*10+dig
    n=n/10
if(temp==rev):
    print("the given number is palindrome")
else:
    print("the number is not a palindrome")
