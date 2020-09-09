num_1 = int(input("Введите число_1 >>>"))
num_2 = int(input("Введите число_2 >>>"))
num_3 = int(input("Введите число_3 >>>"))


def my_func(num_1, num_2, num_3):  # Сумма двух наибольших чисел
    if num_1 < num_2 and num_1 < num_3:
        return num_2 + num_3
    if num_2 < num_1 and num_2 < num_3:
        return num_1 + num_3
    if num_3 < num_1 and num_3 < num_2:
        return num_1 + num_2


print(f"Сумма двух наибольших чисел: {my_func(num_1, num_2, num_3)}")
