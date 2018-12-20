lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
 for num in range(lower,upper + 1):
  if num > 1:
       for a in range(2,num):
           if (num % a) == 0:
               break
       else:
           print(num)
