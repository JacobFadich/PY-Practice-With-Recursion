# Write code for algorithm 2 below
def numbers(x,a=1):
  if a > x:
    return
  else:
    print(a)
    numbers(x,a+1)
numbers(5)