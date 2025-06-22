# Single Inheritance

class College:
    def __init__(self, cname, caddr, no_of_dept):
        self.cname = cname
        self.caddr = caddr
        self.no_of_dept = no_of_dept

    def display_clg_info(self):
        print(f'Name :{self.cname} \t caddr : {self.caddr}\t '
              f'Department count : {self.no_of_dept}')
