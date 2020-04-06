class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name : ", self.name)

    def get_name(self):
        return self.name


class PythonStudent(Student):
    def __init__(self, name, marks):
        Student.__init__(self, name)
        self.theory_marks = marks

    def __str__(self):
        return f"{self.name} - {self.theory_marks}"

    # Overriding
    def show(self):
        super().show()
        print("Theory Marks : ", self.theory_marks)

    def get_marks(self):
        return self.theory_marks


class JavaStudent(Student):
    def __init__(self, name, title, marks):
        super().__init__(name)
        self.project_title = title
        self.project_marks = marks

    def __str__(self):
        return f"{self.name} - {self.project_title} - {self.project_marks}"


p = PythonStudent("Scott", 90)
print(p.get_name(), p.get_marks())

j = JavaStudent("Steve", "Library", 80)
#  print(j)
