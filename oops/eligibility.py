from MyExceptions.custom_exception import Agelimiterror

per_name=input("Enter your name: ")
per_age=int(input("Enter your age: "))
try:
    if per_age<18:
        raise Agelimiterror('Not Eligible!!')
except Agelimiterror as ale:
    print(ale)
else:
    print('Your are eligible to vote.')
finally:
    print("Execution finished!")