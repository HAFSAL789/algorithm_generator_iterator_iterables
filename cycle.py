def cycle(cycle_list):
    length = len(cycle_list)
    start = 0
    while True:
        if start > length-1:
            start = 0
        yield cycle_list[start]
        start += 1
countries = ["Germany", "Switzerland", "Austria"]
country_iterator = cycle(countries)
for i in range(7):
    print(next(country_iterator))

