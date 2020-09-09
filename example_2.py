user_name = input("Введите имя пользователя>>>")
user_surname = input("Введите фамилию пользователя>>>")
user_birth_yaer = input("Введите год рождения пользователя>>>")
user_city_residence = input("Введите город проживания пользователя>>>")
user_e_mail = input("Введите e-mail пользователя>>>")
user_phone = input("Введите телефон пользователя>>>")


def my_func(**kwargs):
    return kwargs


print(my_func(name=user_name, surname=user_surname, birth_year=user_birth_yaer, city_residence=user_city_residence,
              e_mail=user_e_mail, phone=user_phone))
