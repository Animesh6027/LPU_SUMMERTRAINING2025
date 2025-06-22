while True:
    try:
        user_input = input("Enter a number: ")
        num=int(user_input)
        print('Great! Your number is {}'.format(num))
        break
    except ValueError:
        print('Invalid input. Try again!')
print('Execution finished')

