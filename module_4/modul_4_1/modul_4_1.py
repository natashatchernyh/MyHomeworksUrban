from math import inf

from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)

# Вывод на консоль:
# 23.0
# Ошибка
# 7.0
# inf
#
# Примечания:
# После импорта from math import inf возврат будет выглядеть так:
#  return inf.
# Деление в задаче обычное - '/'.
# Не забудьте при импорте функций divide из разных модулей
# переопределить их названия.