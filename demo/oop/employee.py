class Employee:
    # Constructor
    def __init__(self, empid, name, job='PROG'):
        # Object attributes
        self.empid = empid
        self.name = name
        self.__job = job  # Private member

    # Methods
    def show(self):
        print(f"Id   : {self.empid}")
        print(f"Name : {self.name}")
        print(f"Job  : {self.__job}")

    def change_job(self, newjob):
        self.__job = newjob


e1 = Employee(1, "Scott")  # Create an object\
# e1._Employee__job = "TL"
e1.change_job("TL")
e1.show()  # Call method
