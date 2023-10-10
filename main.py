class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции {self.avg_rate()} " \
               f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}"

    def avg_rate(self):
        tmp = []
        for i in self.grades:
            tmp += self.grades[i]
        avg = sum(tmp) / len(tmp)
        return avg
    def add_raring_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.courses_attached:
                if grade <= 10 and grade > 0:
                    if course in lecturer.grades:
                        lecturer.grades[course] += [grade]
                    else:
                        lecturer.grades[course] = [grade]
                else:
                    return 'Значение оценки должно быть от 0 до 10'
            else:
                return 'Лектор не ведет этот курс'
        else:
            return 'Ошибка'




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        return f"{self.name}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__( name, surname)
        self.courses_attached = []
        self.grades = {}
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции {self.avg_rate()}"
    def avg_rate(self):
        tmp = []
        for i in self.grades:
            tmp += self.grades[i]
        avg = sum(tmp) / len(tmp)
        return avg


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('John', 'Smith')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['JS']

best_student.add_raring_lecturer(cool_lecturer, 'Python', 5)
best_student.add_raring_lecturer(cool_lecturer, 'Python', 10)
best_student.add_raring_lecturer(cool_lecturer, 'Python', 6)
best_student.add_raring_lecturer(cool_lecturer, 'JS', 6)
best_student.add_raring_lecturer(cool_lecturer, 'JS', 6)


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 5)
cool_reviewer.rate_hw(best_student, 'Git', 5)
cool_reviewer.rate_hw(best_student, 'Git', 10)

# print(best_student.grades)
# print(cool_lecturer)
print(best_student.grades)
# print(cool_reviewer)
# print(cool_reviewer)