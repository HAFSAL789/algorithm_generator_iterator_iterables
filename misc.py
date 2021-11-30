def pipeline():
    list_of_civilization = ['mesopotomia','egypt','indus valley','mayan']
    civilization_generator = (civilization for civilization in list_of_civilization)
    city_of_civilization = {'mesopotomia':['uruk','ubaid','asyrians','akadians','sumerians','hitties','babylon'],'egypt':['a','b','c']}
    city_generator = (i for civil in civilization_generator for i in city_of_civilization[civil])
    return city_generator

pipeline_1 = pipeline()
def b():
    yield from a()

def a():# sending and printing
    l = yield 10
    print(l)
    # for i in a()
    #
    yield from a()
k = a()
for i in k:
    print(i)
    k.send(11)



def sums(n,name):#coroutine show case
    s = 0
    while n>0:
        s += n
        n -= 1
        # print(f'{name} s = {s} ')
        yield
    return s



def corouti():
    result = yield from sums(10,"sum")
    # print(result)
    print(f'result = {result}')
    #u can create an event loop using yield from

class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        return self

    def __next__(self): # Python 2: def next(self)
        self.current += 1
        if self.current < self.high:
            return self.current
        raise StopIteration


c = Counter(3, 9)

# # class PowTwo:
# #     """Class to implement an iterator
# #     of powers of two"""
# #
# #     def __init__(self, max=0):
# #         self.max = max
# #
# #     def __iter__(self):
# #         self.n = 0
# #         return self
# #     def __reversed__(self):
# #         return "FS"
# #
# #     def __next__(self):
# #         if self.n <= self.max:
# #             result = 2 ** self.n
# #             self.n += 1
# #             return result
# #         else:
# #             raise StopIteration