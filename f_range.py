def frange(*args):
    start = 0
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError(f'got {len(args)} arguments, expected 3')
    value = start
    factor = -1 if step < 0 else 1
    while (value - stop) * (factor) < 0:
        yield value
        value += step

for i in frange(5.6):
    print(i, end=", ")
print()
for i in frange(0.3, 5.6):
    print(i, end=", ")
print()
for i in frange(0.3, 5.6, 0.8):
    print(i, end=", ")
print()
for i in frange(100,10,-1):
    print(i,end=', ')





