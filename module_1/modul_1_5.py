#  "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = 1, 20, 300, 4.0, 40.10, 'apple', True
print(immutable_var)
immutable_var = 1, 20, 300, 4.0, 40.10, 'apple', True + 123456
print(immutable_var)
immutable_var = 1, 20, 300, 4.0, 40.10, 'apple', True * 3      #почему изменилось на 3?
print(immutable_var)
immutable_var = (1, 20, 300, 4.0, 40.10, 'apple', True) + (123456, 456)
print(immutable_var)
immutable_var = (1, 20, 300, 4.0, 40.10, 'apple', True) * 3
print(immutable_var)
print(type(immutable_var))
print(immutable_var[2])
immutable_var[3] = 400
print(immutable_var)

mutable_list = [1, 20, 300], 4.0, 40.10, 'grape', True
print(mutable_list)
mutable_list[0][2] = 'modified'
print(mutable_list)

mutable_list = [1, 20, 300], 4.0, 40.10, 'grape', True
print(type(mutable_list[0]))
print(type(mutable_list))



