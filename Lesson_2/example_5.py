# рейтинг
rating = [5, 5, 5, 4, 3, 2, 1]

level = int(input("Оцените уровень от 1 до 5>>>"))

num = rating.index(level)

count = rating.count(level)

pos = num + count

rating.insert(pos, level)

print(rating)
