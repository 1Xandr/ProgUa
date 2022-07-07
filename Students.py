class Students:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'


class Group:

    def __init__(self):
        self.group = []

    def __iadd__(self, other):
        if isinstance(other, Students):
            if not other in self.group:
                self.group.append(other)
        return self

    def __iter__(self):
        return StudentsIter(self.group)


class StudentsIter:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        raise StopIteration

    def __iter__(self):
        return self


st_1 = Students('Alex')
st_2 = Students('Oleh')
gr_1 = Group()
gr_1 += st_1
gr_1 += st_2

for person in gr_1:
    print(person)