from HomeworkHuman import Human


class Student(Human):

    def __init__(self, name, age, cours=int):
        super().__init__(name, age)
        self.cours = cours

    def __str__(self):
        return super().__str__() + f' Cours = {self.cours}\n'

