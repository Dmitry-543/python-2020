number = int(input("Введите количество секунд"))

hour = number // 3600

number = number % 3600

minute = number // 60

secunde = number % 60

print(f"{hour}:{minute}:{secunde}")
