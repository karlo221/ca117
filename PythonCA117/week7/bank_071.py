class BankAccount:
    def set_attributes(self, name, number, balance=0):
        self.name = name
        self.number = number
        self.balance = balance

    def print_attributes(self):
        print('Name:', self.name)
        print('Account number:', self.number)
        print(f'Balance: {self.balance:.2f}')

    def deposit(self, ammount):
        self.balance = self.balance + ammount
