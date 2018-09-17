print("Enter '0' for exit.");
c= input("Enter any character: ");
if c == '0':
    exit();
else:
    if((c>='a' and c<='z') or (c>='A' and c<='Z')):
    	print(c, "is an alphabet.");
    else:
    	print(c, "is not an alphabet.");
