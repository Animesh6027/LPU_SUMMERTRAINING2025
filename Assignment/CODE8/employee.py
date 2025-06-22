class Employee:
    def __init__(self, empid, name, salary):
        self.__empid = empid
        self.__name = name
        self.__salary = salary

    def get_empid(self):
        return self.__empid
    def set_empid(self, empid):
        self.__empid = empid
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        print('\n---Employee Info---')
        print('Employee ID: ', self.get_empid())
        print('Name:', self.get_name())
        print('Salary:', self.get_salary())

    def apply_hike(self, percentage):
        if percentage < 0:
            raise ValueError('Percentage must be positive')
        hike_amount = self.__salary * (percentage / 100)
        self.__salary += hike_amount
        print('\nSalary after hike: ', self.get_salary())