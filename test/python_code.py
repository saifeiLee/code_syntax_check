def func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


func(a=1, b=2, c=3)


def make_incrementor(n):
    return lambda x: x + n


inc = make_incrementor(42)
# print(inc(42)) # 84