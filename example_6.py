income = int(input("Введите сумму доходов Вашей фирмы"))

expenses = int(input("Введите сумму расходов Вашей фирмы"))

profit = income - expenses

if profit < 0:
    print("Ваша фирма убыточна!!!")
    # break
if profit == 0:
    print("Ваша фирма работает в ноль!!!")
elif profit > 0:

    rent = profit / income
    print(f"Рентабельность Вашей фирмы: {round(rent, 2)}")
    print("Поздравляем! У Вас преуспевающая фирма!!!")

    quantity = int(input("Введите количество сотрудников Вашей фирмы"))

    person_profit = profit / quantity

    print(f"Прибыль Вашей фирмы в расчете на одного сотрудника: {round(person_profit, 2)}")
