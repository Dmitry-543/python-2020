# обмен значений соседних символов
two_list = []

my_list = input("Введите значения")

two_list.extend(my_list)

j = 0
for i in range(int(len(two_list) / 2)):
    two_list[j], two_list[j + 1] = two_list[j + 1], two_list[j]
    j += 2

print(two_list)
