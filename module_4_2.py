def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() # """При вызове функции inner_function() внутри test_function(), мы ничего не увидим в консоли,
                     # так как результат вывода существует только внутри функции test_function(). Чтобы увидеть
                     # результат работы inner_function(), нужно вызвать test_function"""

inner_function()     # """При выводе inner_function() вне функции test_function получим ошибку, так как
                     # inner_function() находится в локальном пространстве имен функции test_function"""

