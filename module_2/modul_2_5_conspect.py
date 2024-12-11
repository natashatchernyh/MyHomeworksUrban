# обычная
def say_hello():
    print("Hello")


say_hello()
say_hello()
say_hello()


# принимающая
def say_hello(name):
    print("Hello", name)


say_hello('m')
say_hello('n')
say_hello('value')


# вызывающая
#import random
#def lottery():
    #tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # win = random.choice(tickets)
    # return win   # равно break
    # print(lottery())
    # win = lottery() + lottery()
    # print(win)

import random
def lottery(mon, tue):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, tue)
    return win1, win2
win1, win2 = lottery('mon', 'tue')
print(win1, win2)

print('------------------------------------------------------------------------------')
# get_matrix и напишите в ней параметры n, m и value

def get_matrix(n, m, volume):
    matrix = []
    for i in range(n):            # i = row
        matrix.append([])
        for j in range(m):               # j = column
            matrix[i].append(volume)
            print(matrix, i, j)
    return matrix
print('-----------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------------')

result=get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result)
print(result2)
print(result3)


print('Мой вариант')
def get_matrix(n, m, volume):
    matrix = []

    for i in range(n):
        matrix.append([])
        print(matrix)               #убрать
        for j in range(m):
            matrix[i].append(volume)
    print(matrix)
    return matrix

get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)



