#iterator-iterable
class FibonacciIterator:
   def __init__(self, limit):
       self.limit = limit
       self.first_value = 0
       self.second_value = 1

   def __iter__(self):
       return self

   def __next__(self):
       if self.limit:
           value = self.first_value
           self.first_value, self.second_value = self.second_value, self.first_value + self.second_value
           self.limit -= 1
           return value
       raise StopIteration

class FibonacciIterable:
   def __init__(self, limit):
       self.limit = limit

   def __iter__(self):
       return FibonacciIterator(self.limit)

Fibonacci_series = FibonacciIterable(10)

for value in Fibonacci_series:
   print(value)

#Infinite Iterator
class FibonacciInfinteIterator:
    def __init__(self):
        self.first_value = 0
        self.second_value = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.first_value
        self.first_value, self.second_value = self.second_value, self.first_value + self.second_value
        return value

# Fibonacci generator
def FibonacciSeriesGenerator(limit):
    first_value = 0
    second_value = 1
    while limit:
        limit -= 1
        value = first_value
        first_value, second_value = second_value, first_value + second_value
        yield value
limit = 10
for value in FibonacciSeriesGenerator(limit):
    print(value)

#send
def FibonacciSeriesGenerator(limit):
    first_value = 0
    second_value = 1
    while limit:
        limit -= 1
        value = first_value
        first_value, second_value = second_value, first_value + second_value
        capture = yield value
        if capture:
            yield capture
limit = 10
FibonacciSeriesGenerator_1 = FibonacciSeriesGenerator(limit)
for count, value in enumerate(FibonacciSeriesGenerator_1):
    print(value)
    if count == limit - 1:
        print(FibonacciSeriesGenerator_1.send(f"First {limit} FibonacciSeries"))

# yield from
first_value = 0
second_value = 1
limit = 10
def FibonacciSeriesRecursive(first_value,second_value,limit):
    if limit:
        yield first_value
        yield second_value
        limit -= 2
        first_value = first_value+second_value
        yield from FibonacciSeriesRecursive(first_value,first_value+second_value,limit)
for value in FibonacciSeriesRecursive(first_value,second_value,limit):
    print(value)

#throw
def FibonacciSeriesInfinite():
    try:
        first_value = 0
        second_value = 1
        while True:
            value = first_value
            first_value, second_value = second_value, first_value + second_value
            yield value
    except StopIteration:
        pass


limit = 10
FibonacciSeriesInfinite_1 = FibonacciSeriesInfinite()
for count, value in enumerate(FibonacciSeriesInfinite_1):
    if count == limit + 1:
        FibonacciSeriesInfinite_1.throw(StopIteration, "limit exceeded")
    print(value)

#close
limit = 10
FibonacciSeriesInfinite_1 = FibonacciSeriesInfinite()
for count, value in enumerate(FibonacciSeriesInfinite_1):
    if count == limit + 1:
        FibonacciSeriesInfinite_1.close()
        print("limit exceeded")
        break
    print(value)

#generator_expression
#only works python 3.8 and beyond because of walrus operator
limit = 10
first_value = 0
second_value = 1
FibonacciSeriesGeneratorExpression = (((value := first_value), (first_value := second_value), (second_value := value + second_value))[0] for _ in
   range(limit))
for value in FibonacciSeriesGeneratorExpression:
    print(value)

#pipelining
limit = 10
first_value = 0
second_value = 1
FibonacciSeriesGeneratorExpression = (
((value := first_value), (first_value := second_value), (second_value := value + second_value))[0] for _ in
range(limit))
fibonacci_gen = (value for value in FibonacciSeriesGeneratorExpression)
fibonacci_pipeline = (f"position = {position}, value = {fibonacci_value} " for position, fibonacci_value in
                    enumerate(fibonacci_gen, 1))
print("FibonacciSeries")
for value in fibonacci_pipeline:
    print(value)
