str1=raw_input("Enter first str:")
str2=raw_input("Enter second str:")
count1=0
count2=0
for i in str1:
   count1=count1+1
for j in str2:
   count2=count2+1
if(count1<count2):
      print("greater str is:")
      print(str2)
elif(count1==count2):
      print("Both str are equal.")
else:
      print("greater str is:")
      print(str1)
