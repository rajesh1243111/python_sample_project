n=int(input('enter a number:'))
if n>1:
 for i in range(2,n):
   if (n%i)==0:
    print(n,'its not prime')
 else:
    print(n,'its prime number')

