# функцию divide, которая принимает два параметра
# first и second. Функция должна возвращать результат деления
# first на second, но когда в second записан 0 - возвращать
# бесконечность

def divide(first, second):
    if second == 0:
        return('inf')
    else:
        return(first/second)

