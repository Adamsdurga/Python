n = int(input("Please Enter the Year Number you wish: "))
 
if (( n%400 == 0)or (( n%4 == 0 ) and ( n%100 != 0))):
    print("%d is a Leap Year" %n)
else:
    print("%d is Not the Leap Year" %n)

