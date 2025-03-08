n = int(input())
sum = 0
for i in range(n):
    inp = int(input())
    sum = sum + inp
average = sum/n 
print("The average is: {:.2f}".format(average))
