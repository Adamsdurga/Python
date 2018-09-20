num = int(input("Enter the value of n: "))
i = num
sum = 0

if num <= 0: 
   print("Enter a whole positive number!") 
else: 
   while num > 0:
        sum = sum + num
        num = num - 1;
    print("Sum of first", i, "natural numbers is: ", sum)
