"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"{self.__class__.__name__}({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if self.denominator == other.denominator:
            self.numerator += other.numerator
        elif not (self.denominator % other.denominator):
            other.numerator = int(self.denominator / other.denominator) * other.numerator
            self.numerator += other.numerator
        elif not (other.denominator % self.denominator):
            self.numerator = int(other.denominator / self.denominator) * self.numerator + other.numerator
            self.denominator = other.denominator
        else:
            self.numerator = (self.numerator * other.denominator
                              + other.numerator * self.denominator)
            self.denominator *= other.denominator

        return f"{self.numerator}/{self.denominator}"


fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
