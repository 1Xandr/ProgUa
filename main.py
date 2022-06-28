from ForError import PeopleError
from HomeworkStudent import Student
from constants import MAX_STUDENT_IN_GROUP as max_st

if __name__ == '__main__':
    class Group:

        def __init__(self, kto):
            self.kto = kto
            self.group_student = []

        def add_student(self, student: Student):
            if len(self.group_student) >= max_st:
                raise PeopleError('students in group must be >10')
            self.group_student.append(student)

        def delete_student(self, student: Student):
            self.group_student.remove(student)

        def search(self, name):
            pes = [i for i in self.group_student if i.name == name]
            return pes if pes else None

        def __str__(self):
            res = ''
            for i in self.group_student:
                tmp = f'{i}'
                res += tmp
            return res


    st_1 = Student('Alex', '19', '3')
    st_2 = Student('Anton', '18', '3')
    st_3 = Student('Andrey', '19', '3')
    st_4 = Student('Vlad', '19', '3')
    st_5 = Student('Vova', '19', '3')
    st_6 = Student('Kostya', '19', '3')
    st_7 = Student('Oleh', '19', '3')
    st_8 = Student('Nazar', '19', '3')
    st_9 = Student('Anatoly', '19', '3')
    st_10 = Student('Avad', '19', '3')
    st_11 = Student('TRY', '0', '0')

    grp = Group('kto')

    grp.add_student(st_1)
    grp.add_student(st_2)
    grp.add_student(st_3)
    # grp.delete_student(st_3)
    # for i in grp.search('Nazar'):
    #     print(i)

    grp.add_student(st_4)
    grp.add_student(st_5)
    grp.add_student(st_6)
    grp.add_student(st_7)
    grp.add_student(st_8)
    grp.add_student(st_9)
    grp.add_student(st_10)
    # grp.add_student(st_11)
    print(grp)
