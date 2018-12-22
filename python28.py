time = float(input("Input time in minutes: "))
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
minutes = time
print("h:m:t-> %d:%d:%d" % ,hour, minutes,time))
