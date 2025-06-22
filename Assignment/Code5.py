str = input("Enter a number: ")
try:
    ans=int(str)
except ValueError:
    print("Invalid input")
else:
    print(ans)
finally:
    print('Execution finished!')