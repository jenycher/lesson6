#Пример использования атрибутов с разным доступом.
#Создаем класс test с прописанной функцией init:

class Test():
    def __init__(self):
        #Создаем публичный атрибут внутри класса:
        self.public = "публичный атрибут"
        #Создаем защищенный атрибут:
        self._protected = "защищенный атрибут"
        #Создаем приватный атрибут:
        self.__private = "приватный атрибут"
    def get_private(self):
        return self.__private

    def set_private(self, value):
        self.__private = value

#Создаем объект класса test:
test = Test()
#Пробуем достать значение из публичного атрибута:
print(test.public)
print(test._protected)

print(test.get_private())
test.set_private("получили значение приватного атрибута")
print(test.get_private())