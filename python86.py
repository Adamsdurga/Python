
m=input("enter input")
flag=0
for j in range(0,len(m)):
    if(m.count(m[j])>1):
        flag=flag+1
if(flag==0):
    print("yes")
else:
    print("no
