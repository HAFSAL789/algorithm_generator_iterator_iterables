def permutations(items):
    if not len(items):
        yield []
    for i in range(len(items)):  # 3 #2 #1
        for each in permutations(items[:i] + items[i + 1:]):  # red 3 - (r) ed -- (e)ed -- d
            # print(each)                                                    --(d) de
            # print(items[i]) #r
            yield [items[i]] + each

for per in permutations(['c','a','r']):
    print(per)
