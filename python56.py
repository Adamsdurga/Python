a=input("Enter Alphanumeric")
x=0
y=0
for char in a:
    if(char.isdigit()):x=x+1
    if(char.isalpha()):y=y+1
  if(x>0 and y>0):
        print('yes')
        break
if(x==0 or y==0):print('No')
