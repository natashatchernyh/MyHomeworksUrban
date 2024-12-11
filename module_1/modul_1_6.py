my_dict = {'Petrov' : 111111, 'Ivanov' : 456789, 'Smirnov' : 987654}
print('My dict: ',my_dict)
Existing_value = my_dict['Petrov']
print('Existing_value: ',Existing_value)
Not_existing_value = my_dict.get('Fedorov')
print('Not-existing_value: ',Not_existing_value)
print('Delated_value: ', my_dict.pop('Petrov'))
my_dict.update({'Popov' : 888666, 'Kovalyov' : 222333})
print('Updated_dict: ',my_dict)

my_set = {11, 22, 5, 2.0, True, 11, 'orange', 5, 'orange', 2.0, True,}
print('my_set: ', my_set)
my_set.add('banana')
my_set.remove(5)     #in set
my_set.discard(7)    # absent in set
print('modified_set: ', my_set)

my_dict = {'Petrov' : 111111, 'Ivanov' : 456789, 'Smirnov' : 987654}
print('My dict: ',my_dict)
Existing_value = my_dict['Petrov']                   # значение по существующему ключу
print('Existing_value: ',Existing_value)
Not_existing_value = my_dict.get('Fedorov')          # по отсутствующему из словаря my_dict
print('Not-existing_value: ',Not_existing_value)
print('Delated_value: ', my_dict.pop('Petrov'))
my_dict.update({'Popov' : 888666, 'Kovalyov' : 222333})  # добавить ве произвольные пары того же формата
print('Updated_dict: ',my_dict)


