def findArmstrong(a, b) : 
      for i in range(low + 1, b) : 
          x = i
             n = 0
        while (x != 0) : 
            x = x / 10
            n = n + 1
      pow_sum = 0 
        x = i 
        while (x != 0) : 
            digit = x % 10
            pow_sum = pow_sum + math.pow(digit, n) 
            x = x / 10
        if (pow_sum == i) : 
            print(str(i) + " "), 
num1 = 100
num2 = 400
findArmstrong(num1, num2) 
print("") 
