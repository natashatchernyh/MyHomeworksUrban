#"Распаковка позиционных параметров".
#-----------------------------------------------------------------------------------------------------------------
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
# print_params(a, b, c, d=7)      #name 'a' is not defined
# print_params(b, c)              #name 'b' is not defined
# print_params(a, b, c)           # name 'a' is not defined

values_list = [1, 'string', True]
values_dict = {'a': 1, 'b': 'string', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)


# Вывод на консоль:
# 54.32 'Строка' 42
# -------------------------------------------------------------------------------------------------------
def a(my_list=[]):  # expected an indented block after function definition on line 26

    def append_to_list(item, list_my=None):
        if list_my is None:
            list_my = []
            list_my.append(item)


print(list_my)  # name 'list_my' is not defined
