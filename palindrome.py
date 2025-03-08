n = int(input())
temp = n
remainder = 0
rev = 0
while (n>0):
  remainder = n%10
  rev = rev*10 + remainder
  n=n//10

if temp == rev:
    print ("The number is a palindrome")
else:
    print ("The number is not a palindrome")
