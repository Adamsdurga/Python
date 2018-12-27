x=int(input("Enter number:"))
count=1
while(x>1):
    count=count+1
    x=x//10
print("The number of digits in the number are:",count)
