x=int(input("enter  no"))
y=int(input("enter  no"))
for j in range(y,0,-1):
    if(x%j==0 and y%j==0):
      print(j)
      break
