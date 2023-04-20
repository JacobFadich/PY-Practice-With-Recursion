# Write code for algorithm 1 below

def counter(x):
    if x==0:
        return
    else:
        print(x)
        counter(x-1)

print(counter(3))



