z1=int(input("Enter 1st number"))
z2=int(input("Enter 2nd number"))
flag=0
prod=z1*z2
for y in range(1,max(n1,n2)+1):
	k=y*y
	if k==prod:
		flag=1
if (flag==0):
	print("NO")
else:
	print("Yes")
