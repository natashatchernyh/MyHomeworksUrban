calls = 0   # глобальная переменная

def count_calls ():     # подсчитыват вызовы остальных функций.
    global calls        # указываем ,что calls это глобальное пространство
    calls += 1          # добавляем на счетчик циклов прохода/функций

def string_info (string):            # принимает аргумент строку
    count_calls()                     # подсчитывает вызов функции, добавляет кол-во в def count calls
    a_len = len(string)                  # длина
    str_upper = string.upper()          # меняем на верхний регистр
    str_lower = string.lower()          # меняем на нижний регистр
    b_tuple = (a_len, str_upper, str_lower)    #переменная для кортежа
    return (b_tuple)        #возвращает кортеж(длина строки, строка в верхнем регистре, строка в нижнем регистре)
                            #?

def is_contains (line, list_to_search):
    count_calls()
    line_lower = line.lower # привести в нижний регистр
    return line_lower in (line() in list_to_search[])


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)