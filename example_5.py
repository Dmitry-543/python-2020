a = int(input("Введите количество километров для тренировки в первый день"))

b = int(input("Введите желаемый уровень тренировки(км) с учетом прогресса 10% в день"))

days = 1

print(f"1-й день: {a} км")

while a < b:
    a = a + a * 0.1
    days = days + 1
    print(f"{days}-й день: {round(a, 2)} км")

print(f"Ответ: на {days}-й день, спортсмен достигнет результата не менее {b} км в день.")
