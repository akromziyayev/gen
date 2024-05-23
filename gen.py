# fibonacci generator
#
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# fibo = fibonacci()
# for i in fibo:
#     print(i)


# # fibonacci iterator
#
# class FibonacciIterator:
#     def __init__(self):
#         self._start = 0
#         self._next = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         fibonacci1 = self._start
#         self._start, self._next = self._next, self._start + self._next
#         return fibonacci1
#
#
# fibo = FibonacciIterator()
# for i in fibo:
#     print(i)


# .send()
#
# def square():
#     while True:
#         value = yield
#         yield value ** 2
#
#
# gen = square()
# a = 1
# for i in range(int(input("range: "))):
#     next(gen)
#     print(f'=> {gen.send(int(input("input: ")))}')


# close
#
# def func():
#     try:
#         yield 1
#         yield 2
#         yield 3
#     except StopIteration:
#         print("GeneratorExit")
#
#
# gen = func()
# print(next(gen))
# gen.close()
# print(next(gen))


# throw
#
# def func():
#     for i in range(1, 25):
#         yield i ** 2
#
#
# gen = func()
# for i in range(int(input("range: "))):
#     print(next(gen))
# gen.throw(ValueError)
