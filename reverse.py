n = int(input())
remainder = 0
rev = 0
while (n>0):
  remainder = n%10
  rev = rev*10 + remainder
  n=n//10
  
print (rev)
