from Assignment.CODE8.employee import Employee

def main():
    print('\n---Employee Management System---')
    emp_id = input('Enter Employee Id: ')
    name = input('Enter Employee Name: ')

    while True:
        try:
            sal = float(input('Enter Salary: '))
            if sal < 0:
                raise ValueError
            break
        except ValueError:
            print('\nInvalid Salary')

    emp = Employee(emp_id, name, sal)

    while True:
        print('\n---Employee Details---')
        print('1. View Employee Details')
        print('2. Apply Hike')
        print('3. Update Employee Details')
        print('4. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            emp.display_info()
        elif choice == 2:
            try:
                percent = float(input('Enter percentage(%): '))
                emp.apply_hike(percent)
            except ValueError as e:
                print('Error:', e)
        elif choice == 3:
            new_name = input('Enter New Name: ')
            emp.set_name(new_name)
        else:
            print('Exiting..Thank You')
            break

if __name__ == '__main__':
    main()