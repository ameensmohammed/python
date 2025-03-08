a = float(input())
b = float(input())
c = float(input())

if (a+b<=c or b+c<=a or c+a<=b):
    print("Invalid Triangle")
else:
   s = (a+b+c)/2
   area = (s*(s-a)*(s-b)*(s-c))**0.5
   print("The area of the triangle is: {:.2f}".format(area))
