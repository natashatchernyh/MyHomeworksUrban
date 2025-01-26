def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")
        print(dir())

        #inner_function()     #Вызовите функцию inner_function внутри функции test_function - ничего не возвращает

    #inner_function()  # Вызовите функцию inner_function внутри функции test_function - ничего не возвращает

#inner_function()   #NameError: name 'inner_function' is not defined. Did you mean: 'test_function'? -