def average_counter():
    total_value = 0
    total_Count = 0
    number = None
    while True:
        value = yield number
        total_Count += 1
        total_value += value
        number = total_value / total_Count

n = average_counter()
next(n)
for value in [7, 13, 17, 231, 12, 8, 3]:
    print(f"sent{value}, new average{n.send(value)}")