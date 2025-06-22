num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
nums = [1,2,3]
try:
    ans=num1//num2
    elmt = nums[1]
except ZeroDivisionError:
    print("Invalid input.")
except IndexError:
    print("Choose Correct Index.")
else:
    print(f'Quotient: {ans}')
    print(f'Remainder: {num1%num2}')
    print(f'Element: {elmt}')
finally:
    print("Execution finished")