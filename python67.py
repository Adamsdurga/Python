import math
m3=int(input("Enter Value"))
if m3<10: print("10")
else:
    l2=len(str(m3))
    m3+=5
    m3=m3/(10**(l2-1))
    print(math.floor(n2)*(10**(l2-1)))
