from Assignment.CODE7.bankaccount import BankAccount

def main():
    account_num = int(input('Enter account number: '))
    holder_name = input('Enter holder name: ')

    while True:
        try:
            initial_balance = float(input('Enter initial balance: '))
            if initial_balance < 0:
                raise ValueError
            break
        except ValueError:
            print('Please enter a valid amount.')

    account = BankAccount(account_num, holder_name, initial_balance)

    while True:
        print('\n--Menu--')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. View account info')
        print('4. Update holder name')
        print('5. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            try:
                amount = float(input('Enter amount to deposit: '))
                account.deposit(amount)
            except ValueError:
                print('Please enter a valid amount.')
        elif choice == '2':
            try:
                amount = float(input('Enter amount to withdraw: '))
                account.withdraw(amount)
            except ValueError:
                print('Please enter a valid amount.')
        elif choice == '3':
            account.display_info()
        elif choice == '4':
            new_holder_name = input('Enter new holder name: ')
            account.set_holder_name(new_holder_name)
            print("Name updated.")
        elif choice == '5':
            print('Exiting.Thank you!')
            break
        else:
            print('Invalid input. Try again!')

if __name__ == '__main__':
    main()

