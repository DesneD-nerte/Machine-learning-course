import math


def f_x(x):
    try:
        y = 1 / (x + 1) + x / (x - 3)
    except:
        y = math.inf

    return y


a: float = float(input("a = "))
b: float = float(input("b = "))
n: int = int(input("n = "))
N: int = int(input("Введите номер варианта = "))

if(n < 0 or a >= b or N < 0):
    print("Ошибочные входные данные")
else:
    h = (b + N - a - N) / (n - 1)

    x_list = [a - N + i * h for i in range(n)]
    f_list = [f_x(x) for x in x_list]

    print("-" * 17)
    print(f"| {"{0:4s} | {1:6s}".format("x", "f(x)")} |")
    print("-" * 17)

    for i in range(n):
        print("| {0:4.1f} : {1:6.3f} |".format(x_list[i], f_list[i]))

    print("-" * 17)


