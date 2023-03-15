def f(a):
    if a == 0:
        return 1
    elif a == 1:
        return 3
    elif a > 1 and a % 2 == 0:
        return f(a - 1) - f(a - 2) + 3 * a
    elif a > 1 and a % 2 != 0:
        return f(a - 2) - f(a - 3) + 2 * a

print(f(40))

