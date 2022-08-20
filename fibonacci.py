# Fibonacci Iterator
class Fibo_Iter:
    '''Iterator of Fibonacci Sequence.
    
    <Arguments> [start,] end (Contains end)'''
    def __init__(self, *args): 
        if len(args) < 1:
            raise TypeError(f"Fibo_Iter expected at least 1 argument, got {len(args)}")
        elif len(args) == 1:
            self.start = 0
            self.end = args[0]
        elif len(args) == 2:
            self.start = args[0]
            self.end = args[1]
        else:
            raise TypeError(f"Fibo_Iter expected at most 2 arguments, got {len(args)}")

        self.count = self.start
        self.prev = 0
        self.current = 1

        for _ in range(self.start):
            self.prev, self.current = self.current, self.prev + self.current
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count > self.end:
            raise StopIteration
        else:
            self.prev, self.current = self.current, self.prev + self.current
            self.count += 1
            return self.current - self.prev
    
    def __str__(self):
        return f"Fibo_Iter({self.start}, {self.end})"

# Fibonacci Generator
def fibo_gen(*args):
    '''Generator of Fibonacci Sequence.
    
    <Arguments> [start,] end (Contains end)'''
    if len(args) < 1:
        raise TypeError(f"fibo_gen expected at least 1 argument, got {len(args)}")
    elif len(args) == 1:
        start = 0
        end = args[0]
    elif len(args) == 2:
        start = args[0]
        end = args[1]
    else:
        raise TypeError(f"fibo_gen expected at most 2 arguments, got {len(args)}")

    count = start
    prev = 0
    current = 1

    for _ in range(start):
        prev, current = current, prev + current
    
    while count <= end:
        yield prev
        prev, current = current, prev + current
        count += 1

# Fibonacci Generator (Recursive)

'''
Why my recursive generator doesn't work?

1. returns (yields) the first value of the list
2. then it creates a new iterator object calling the same generator function, passing a slice of the list to it
3. and then stops
'''

def fibo_recursive_gen(*args):
    '''Recursive Generator of Fibonacci Sequence.
    
    <Arguments> [start,] end (Contains end)'''
    if len(args) < 1:
        raise TypeError(f"fibo_gen expected at least 1 argument, got {len(args)}")
    elif len(args) == 1:
        start = 0
        end = args[0]
    elif len(args) == 2:
        start = args[0]
        end = args[1]
    else:
        raise TypeError(f"fibo_gen expected at most 2 arguments, got {len(args)}")

    prev = 0
    current = 1

    for _ in range(start):
        prev, current = current, prev + current

    if start >= end:
        yield prev
    else:
        yield prev
        for i in fibo_recursive_gen(start + 1, end):
            yield i
