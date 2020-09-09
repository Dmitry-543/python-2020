def div_num(): # Деление первого числа на второе
    try:
        a = int(input("Введите первое число>>> "))
        b = int(input("Введите второе число>>> "))
        c = a / b
        return c
    except:
        return (f"На ноль делить нельзя!!!")


print(f"Результат деления: {div_num()}")
