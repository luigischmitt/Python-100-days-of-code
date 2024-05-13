def add(*args):
    soma = 0
    for n in args:
        soma += n
    return soma

# print(add(1, 2, 3, 4))

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
