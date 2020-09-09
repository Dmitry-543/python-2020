word = input("Введите слово>>>")


def int_func(word):
    word_mod = word.title()
    return word_mod


print(int_func(word))

sentence = input("Введите предложение>>>")

print(int_func(sentence))
