class BankAccount:
    def __init__(self, account_num, holder_name, balance=0.0):
        self.__account_num = account_num
        self.__holder_name = holder_name
        self.__balance = balance
    def get_account_num(self):
        return self.__account_num
    def set_account_num(self, account_num):
        self.__account_num = account_num
    def get_holder_name(self):
        return self.__holder_name
    def set_holder_name(self, holder_name):
        self.__holder_name = holder_name
    def get_balance(self):
        return self.__balance
    def set_balance(self, balance):
        if balance < 0:
            raise ValueError('Balance must be greater than 0')
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited {amount:.2f}. New balance: {self.__balance:.2f}')
        else:
            raise ValueError('Deposited amount must be positive')

    def withdraw(self, amount):
        if amount <=0:
            raise ValueError('Amount must be greater than 0')
        elif amount > self.__balance:
            raise ValueError('Amount must be greater than balance')
        else:
            self.__balance -= amount
            print(f'Withdrawed {amount:.2f}. New balance: {self.__balance:.2f}')

    def display_info(self):
        print('\n ---Account Details---')
        print(f'Account Number: {self.__account_num}')
        print(f'Holder Name: {self.__holder_name}')
        print(f'Balance: {self.__balance:.2f}')
        print('********************')


