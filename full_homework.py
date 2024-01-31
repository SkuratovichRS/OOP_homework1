class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectors(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {average_rate(self)}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенные курсы: Введение в программирование')

    def __lt__(self, other):
        return average_rate(self) < average_rate(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average_rate(self)}'

    def __lt__(self, other):
        return average_rate(self) < average_rate(other)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


def average_rate(stud_or_lect):
    rate_sum = 0
    marks_count = 0
    for item in stud_or_lect.grades.values():
        rate_sum += sum(item)
        marks_count += len(item)
    if rate_sum != 0 and marks_count != 0:
        return round(rate_sum / marks_count, 2)
    else:
        return 0


def all_stud_hw_av(students_list, course):
    rate_sum = 0
    marks_count = 0
    for student in students_list:
        if course in student.grades:
            rate_sum += sum(student.grades[course])
            marks_count += len(student.grades[course])
    if rate_sum != 0 and marks_count != 0:
        return round(rate_sum / marks_count, 2)
    else:
        return 0


def all_lect_rate_av(lectures_list, course):
    rate_sum = 0
    marks_count = 0
    for lecturer in lectures_list:
        if course in lecturer.grades:
            rate_sum += sum(lecturer.grades[course])
            marks_count += len(lecturer.grades[course])
    if rate_sum != 0 and marks_count != 0:
        return round(rate_sum / marks_count, 2)
    else:
        return 0





stud1 = Student('Roman', 'Skuratovich', 'M')
stud1.courses_in_progress += ['Python', 'Java']
stud2 = Student('Small', 'Woman', 'W')
stud2.courses_in_progress += ['Python', 'Astronomy']
lect1 = Lecturer('Ivan', 'Ivanov')
lect1.courses_attached += ['Python', 'Java']
lect2 = Lecturer('Big', 'Man')
lect2.courses_attached += ['Python', 'Astronomy']
rev1 = Reviewer('Jessy', 'Pinkman')
rev1.courses_attached += ['Python', 'Java', 'Astronomy']
rev2 = Reviewer('Jessica', 'Alba')
rev2.courses_attached += ['Python', 'Astronomy']

stud1.rate_lectors(lect1, 'Python', 9)
stud2.rate_lectors(lect2, 'Astronomy', 9)
stud2.rate_lectors(lect2, 'Python', 8)
rev1.rate_hw(stud1, 'Java', 7)
rev2.rate_hw(stud2, 'Python', 10)
rev2.rate_hw(stud1, 'Python', 10)
print(stud1)
print(stud1 < stud2)
print(lect2)
print(lect2 == lect1)
print(rev1)

print(all_stud_hw_av([stud1, stud2], 'Python'))
print(all_lect_rate_av([lect1, lect2], 'Python'))