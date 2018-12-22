def largest(arr,a): 
    max = arr[0] 
  for i in range(1, a): 
        if arr[i] > max: 
            max = arr[i] 
    return max
arr = [10, 324, 45, 90, 9808] 
a = len(arr) 
Ans = largest(arr,a) 
print ("Largest in given array is",Ans) 
