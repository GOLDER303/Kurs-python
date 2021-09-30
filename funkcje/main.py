def a():
    pass # nie robi nic jest tylko po to zeby kod sie nie wywalił

def b():
    return 2, 3, 4

b()


def c(a):
    return a * a

print(c(5))


def d(a, b = 5):
    return a * b 

print(d(10))
print(d(10, b = 20))


def e(text: str) -> str:
    return text

print(e("napis"))


def a(*args):
    for arg in args:
        print(arg)

a(2, 6, 'ta', 1, ['t', 'a']) #args to lista


def a(**kwargs):
    result = 0
    for kwarg in kwargs:
        result += kwargs[kwarg]
    print(result)

a(v = 2, c = 4, x = 5) #kwargs to słownik


def a (*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for kwarg in kwargs:
        result += kwargs[kwarg]
    print(result)

a(2, 3, 4, v = 1, z = 4, e = 2)