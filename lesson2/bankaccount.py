"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    def __init__(self, balance):
        """
        Конструктор, принимающий начальный баланс счета.
        balance: свойство, которое возвращает текущий баланс счета.
        """
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount):
        """
        Метод, который позволяет внести деньги на счет.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Метод, который позволяет снять деньги со счета.
        """
        self.balance -= amount

    def close(self):
        """
        Метод, который закрывает счет и возвращает оставшиеся на нем деньги
        :return:
        """
        out_data = self.balance
        self.balance = 0
        return out_data


account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
