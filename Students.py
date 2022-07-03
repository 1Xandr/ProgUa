class Human:

    def __init__(self, name=str, age=int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name = {self.name}, Age = {self.age},'


class Student(Human):

    def __init__(self, name, age, kurs=int):
        super().__init__(name, age)
        self.kurs = kurs

    def __str__(self):
        return super().__str__() + f' Cours = {self.kurs}\n'


MAX_STUDENTS_IN_GROUP = 3


class Group:

    def __init__(self):
        self.group_student = []

    # def add_student(self, student: Student):
    #     if len(self.group_student) < MAX_STUDENTS_IN_GROUP:
    #         self.group_student.append(student)
    #
    # def delete_student(self, student: Student):
    #     self.group_student.remove(student)

    def __iadd__(self, other):
        if len(self.group_student) < MAX_STUDENTS_IN_GROUP:
            if isinstance(other, Student):
                self.group_student.append(other)
        return self

    def __isub__(self, other):
        if isinstance(other, Student):
            self.group_student.remove(other)
        return self

    def __str__(self):
        res = ''
        for i in self.group_student:
            tmp = f'{i}'
            res += tmp
        return res


st_1 = Student('Alex', '19', '3')
st_2 = Student('Anton', '18', '3')
st_3 = Student('Andrey', '19', '3')

grp = Group()

grp += st_1
grp += st_2
grp += st_3
grp -= st_3

print(grp)