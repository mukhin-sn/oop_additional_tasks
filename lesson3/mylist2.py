"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""


class MyList2:
    def __init__(self, data, start=0, step=1):
        self.data = data
        self.__start = start
        self.__step = step

    def __iter__(self):
        self.__current_value = self.__start - self.__step
        return self

    def __next__(self):
        if self.__current_value + self.__step < len(self.data):
            self.__current_value += self.__step
            return self.data[self.__current_value]
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.data[index]


my_list = MyList2([1, 2, 3])
for i in my_list:
    print(i)  # 1 2 3

print(my_list[1])  # 2
