c1 = float(input("Enter first number: "))
c2 = float(input("Enter second number: "))
c3 = float(input("Enter third number: "))
 
if (c1 > c2) and (c1 > c3):
   largest = c1
elif (c2 > c1) and (c2 > c3):
   largest = c2
else:
   largest = c3
 
print("The largest number is",largest)
