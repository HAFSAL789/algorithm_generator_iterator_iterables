import random
def random_ones_and_zeros():
    p = 0.5
    while True:
        value = random.random()
        recieved = yield 1 if value < p else 0
        if recieved:
            p = recieved
x = random_ones_and_zeros()
next(x)
for p in [0.2, 0.8]:
    print("\nWe change the probability to : " + str(p))
    x.send(p)
    for i in range(20):
        print(next(x), end=" ")