x=input("calculator")
try:
  k=x.split("/")
  print(int(k[0])/int(k[1]))
except:
    k = x.split("%")
    print(int(k[0])%int(k[1]))
