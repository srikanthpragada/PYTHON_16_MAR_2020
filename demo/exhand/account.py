class BalanceError(Exception):
    def __init__(self, message="Insufficient Balance"):
        self.message = message

    def __str__(self):
        return self.message


class Account:
    def __init__(self, acno, name, balance):
        self.acno = acno
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise BalanceError(f"Balance is {self.balance} but you tried to withdraw {amount}")


a = Account(1, "Abc", 10000)
try:
    a.withdraw("43434")
except BalanceError as ex:
    print(ex)
except Exception as ex:
    print("Unknown Error ", ex)
