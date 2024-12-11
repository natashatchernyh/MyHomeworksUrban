from logging.config import stopListening

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # выписывать из этого списка только положительные числа
i = 0  # index -
while i < len(my_list):
    if my_list[i] < 0:
        break
    if my_list[i] > 0:
        print(my_list[i])
    i += 1  # шаг при переборе
