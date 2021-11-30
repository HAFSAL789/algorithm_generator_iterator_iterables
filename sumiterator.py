class SumIterator:
    def __init__(self,max_value):
        self.max_value = max_value
        self.sum = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_value:
            self.sum += self.max_value
            self.max_value -= 1
            return self.sum
        raise StopIteration

# print(list(SumIterator(100000000000000000000))
# # print(range(0, 100))
for i in SumIterator(100000000000000000000):
    print(i)