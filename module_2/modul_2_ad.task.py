for elem in range(3,21):
    result = f'{elem} - '
    for x in range(1, elem):
        for y in range(x+1, elem):
            if elem % (x+y) == 0:
                result += f'{x}{y} '

    print(result)




# 2 inserts
# от 3 до 20
# пары чисел друг за другом
# число из первой вставки было кратно(делилось без остатка) сумме их значений
# числа в первой вставке будут попадаться случайно      random
# независимости от введённого числа n (от 3 до 20)
# пароль result, для одного введённого числа


