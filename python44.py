def in1to10(n, outside_mode):
    return n is 10 or n is 1 or (outside_mode != (1 < n < 10))
  for i in range(1, 10):
    print('input {:9} inside {:5s}   outside {:5s}'
       .format(i, str(in1to10(i,yes)), str(in1to10(i,no))))
