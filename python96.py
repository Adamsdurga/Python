m=int(input("Enter the numbers:"))
if m>1:
    for i in range(2,m):
        if m%i==0:
            print ('Yes')
            break
    else:
        print("no")
elif m==1 or m==0:
  print ('neither prime nor composites')
