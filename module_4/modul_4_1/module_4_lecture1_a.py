# import module_4_lecture1_b as m4_b      # можем дать псевдоним
# print(dir(m4_b))     # можем увидеть все атрибуты и переменные из модуля b
#
# print('Привет, я из модуля 1')
# m4_b.say_hi()
# print(m4_b.a)    # вызов переменной из модуля b


from module_4_lecture1_b import *     # можем все импортировать из второго модуля
print('Привет, я из модуля 1')
say_hi()
print(a)
print(b)


#from module_4_lecture1_b import a,b, say_hi     # можем импортировать отдельные переменные из второго модуля




