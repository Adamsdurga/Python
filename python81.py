def do_stuff(input):
x,y = [int(x) for x in input.split(" ")]
print(y-x)
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
