grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]      #список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  #множество
a = sum(grades[0]) / len(grades[0])
b = sum(grades[1]) / len(grades[1])
c = sum(grades[2]) / len(grades[2])
d = sum(grades[3]) / len(grades[3])
e = sum(grades[4]) / len(grades[4])
grades_mod = [a, b, c, d, e]
print(grades_mod)

students_2nd = sorted(students)
print(students_2nd)

print(dict(zip(students_2nd, grades_mod)))
print('Control_point:', {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8})



students_mod = list([students])
print(type(students_mod))
students_new = sorted(students_mod)
print(type(students_new))

print(dict(zip(students, grades_mod)))



st_dict = {'key1' : 'values1', 'key2' : 'values2'}
st_dict.update({'четыре' : 8, 'два' : 2, 'н/а' : 0})  # добавить
print(st_dict)

a = st_dict.pop('четыре')
print(st_dict)
print(a)

print(st_dict.keys())
print(st_dict.values())
print(st_dict.items())




