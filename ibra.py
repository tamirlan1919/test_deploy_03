#Напиши здесь код

# Функция для извлечения запретных символов
def func(name):
    zapret_symbol = "\"\\\'!#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"
    new_st = ''
    for i in name:
        if i not in zapret_symbol:
            new_st += i
        else:
            pass

    return new_st


print(func('Ибр@$@аг52@%и"4к2'))