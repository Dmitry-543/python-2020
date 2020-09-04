#разбить текст на строки(максимум 10 символов), строки пронумеровать
text = input("Введите текст!>>>")

text = text.split()

i = 0

while i < len(text):
    text_print = text[i]
    print(f"{i + 1}.{text_print[:10]}")

    i = i + 1
