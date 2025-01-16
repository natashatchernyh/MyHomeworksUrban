
import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)

def add():
    num1,num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1,num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1,num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1,num2 = get_values()
    res = num1 * num2
    insert_values(res)



window = tk.Tk()
window.title('Калькулятор')
window.geometry("450x450")
window.resizable(False,False)

button_add = tk.Button(window, text = "+", width=2, height=2, command = add)     # создали элемент, но не расположили на самом "калькуляторе"
button_add.place(x=100, y=200)                  # расположили пустую кнопку по указанным координатам

button_sub = tk.Button(window, text = "-", width=2, height=2, command = sub)    # создали элемент, но не расположили на самом "калькуляторе"
button_sub.place(x=150, y=200)                  # расположили пустую кнопку по указанным координатам

button_mul = tk.Button(window, text = "*", width=2, height=2, command = mul)     # создали элемент, но не расположили на самом "калькуляторе"
button_mul.place(x=200, y=200)                  # расположили пустую кнопку по указанным координатам

button_div = tk.Button(window, text = "/", width=2, height=2, command = div)     # создали элемент, но не расположили на самом "калькуляторе"
button_div.place(x=250, y=200)                  # расположили пустую кнопку по указанным координатам

number1_entry = tk.Entry(window, width = 50,)
number1_entry.place(x = 50, y = 75)

number2_entry = tk.Entry(window, width = 50,)
number2_entry.place(x = 50, y = 150)

answer_entry = tk.Entry(window, width = 50,)
answer_entry.place(x = 50, y = 300)

number1 = tk.Label(window, text = "Введите первое число:")
number1.place(x=100,  y = 50)
number2 = tk.Label(window, text = "Введите второе число:")
number2.place(x=100,  y = 115)
answer_entry = tk.Label(window, text = "Ответ")
answer_entry.place(x = 20, y = 270)

window.mainloop()

# C:\Users\User\AppData\Local\Programs\Python\Python310\python.exe D:\PycharmProjects\MyHomeworkUrban\module_3\calc.py
# Exception in Tkinter callback
# Traceback (most recent call last):
#   File "C:\Users\User\AppData\Local\Programs\Python\Python310\lib\tkinter\__init__.py", line 1921, in __call__
#     return self.func(*args)
#   File "D:\PycharmProjects\MyHomeworkUrban\module_3\calc.py", line 15, in add
#     insert_values(res)
#   File "D:\PycharmProjects\MyHomeworkUrban\module_3\calc.py", line 9, in insert_values
#     answer_entry.delete(0, 'end')
# AttributeError: 'Label' object has no attribute 'delete'
#
# Process finished with exit code 0
