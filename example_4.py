#_1_вариант

x = float(input("Введите положительное число!>>>"))
y = int(input("Введите целое отрицательное число!>>>"))


def multy_num(x, y): # Возведение числа "x" в степень 'y"
    y = abs(y)
    return x ** y


print(int(multy_num(x, y)))

# _2_вариант

#x = float(input("Введите положительное число!>>>"))
#y = int(input("Введите целое отрицательное число!>>>"))


def my_func(x, y):  # Возведение числа "x" в степень 'y"
    y = abs(y)
    i = 1
    multy_x = 1
    while i <= y:
        multy_x = multy_x * x
        i = i + 1
    return int(multy_x)


print(f"Результат возведения 'x' в степень 'y': {my_func(x, y)}")

