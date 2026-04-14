class BankAccount:
    def __init__(self,login,balance,password):
        self.login = login
        self._balance = balance
        self.password = password
    def get_balance(self,password):
        if password == self.password:
            return self._balance
        else:
            return 'Неверный пороль '



ardager = BankAccount(login="ardager",balance=10000,password="1111")
print(ardager._balance)
print(ardager.login)
print(ardager.password)