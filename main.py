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

    def __eq__(self, other):
        if self.avg_rate() > other.avg_rate():
            return f"Имя: {self.name} балл: {self.avg_rate()}"
        elif self.avg_rate() < other.avg_rate():
            return f"Имя: {other.name} балл: {other.avg_rate()}"
        else:
            return f"Баллы одинаковые у {self.name} и {other.name}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        return f"{self.name}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции {self.avg_rate()}"

    def __eq__(self, other):
        if self.avg_rate() > other.avg_rate():
            return f"Студент: {self.name} {self.surname}.\nСредний балл: {self.avg_rate()}"
        elif self.avg_rate() < other.avg_rate():
            return f"Студент: {other.name} {other.surname}.\nСредний балл: {other.avg_rate()}"
        else:
            return f"Баллы одинаковые у {self.name} {self.surname} и {other.name} {other.surname}.\nСреднее количество баллов: {other.avg_rate()}"
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

def all_grade_students(course, student_list):
    tmp_list = []
    for student in student_list:
        if course in student.grades.keys():
            for grade in student.grades[course]:
                tmp_list.append(grade)
        else:
            print(f'У студента {student.name} нет курса {course}')
    avg_grade = sum(tmp_list) / len(tmp_list)
    return f"Средняя оценка за курс {course} у студентов: {avg_grade}"

def all_grade_lectors(course, lectors_list):
    tmp_list = []
    for student in lectors_list:
        if course in student.grades.keys():
            for grade in student.grades[course]:
                tmp_list.append(grade)
        else:
            print(f'У лектора {student.name} нет курса {course}')
    avg_grade = sum(tmp_list) / len(tmp_list)
    return f"Средняя оценка за курс {course} у лектора: {avg_grade}"

best_student = Student('Ruoy', 'Eman', 'Male')
best_student_two = Student('Erman', 'Chekovskiy', 'Male')
best_student.courses_in_progress += ['Python']
best_student_two.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student_two.courses_in_progress += ['Git']
best_student.finished_courses += ['Git']
best_student_two.finished_courses += ['Git']

cool_reviewer = Reviewer('Igor', 'Gatsky')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_lecturer = Lecturer('John', 'Smith')
cool_lecturer_two = Lecturer('Stein', 'Silver')
cool_lecturer_two.courses_attached += ['Python']
cool_lecturer_two.courses_attached += ['JS']
cool_lecturer_two.courses_attached += ['Git']
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['JS']
cool_lecturer.courses_attached += ['Git']

best_student.add_raring_lecturer(cool_lecturer, 'Python', 5)
best_student_two.add_raring_lecturer(cool_lecturer, 'Python', 2)
best_student.add_raring_lecturer(cool_lecturer, 'Python', 10)
best_student_two.add_raring_lecturer(cool_lecturer, 'Python', 9)
best_student.add_raring_lecturer(cool_lecturer, 'Python', 6)
best_student_two.add_raring_lecturer(cool_lecturer, 'Python', 1)
best_student.add_raring_lecturer(cool_lecturer, 'JS', 6)
best_student_two.add_raring_lecturer(cool_lecturer, 'JS', 2)
best_student.add_raring_lecturer(cool_lecturer, 'JS', 6)
best_student_two.add_raring_lecturer(cool_lecturer, 'JS', 10)

best_student.add_raring_lecturer(cool_lecturer_two, 'Python', 5)
best_student_two.add_raring_lecturer(cool_lecturer_two, 'Python', 10)
best_student.add_raring_lecturer(cool_lecturer_two, 'Python', 4)
best_student_two.add_raring_lecturer(cool_lecturer_two, 'Python', 5)
best_student.add_raring_lecturer(cool_lecturer_two, 'Python', 6)
best_student_two.add_raring_lecturer(cool_lecturer_two, 'Python', 1)
best_student.add_raring_lecturer(cool_lecturer_two, 'JS', 1)
best_student_two.add_raring_lecturer(cool_lecturer_two, 'JS', 6)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student_two, 'Python', 2)
cool_reviewer.rate_hw(best_student, 'Python', 3)
cool_reviewer.rate_hw(best_student_two, 'Python', 4)
cool_reviewer.rate_hw(best_student, 'Python', 1)
cool_reviewer.rate_hw(best_student_two, 'Python', 2)
cool_reviewer.rate_hw(best_student, 'Git', 3)
cool_reviewer.rate_hw(best_student_two, 'Git', 7)
cool_reviewer.rate_hw(best_student, 'Git', 6)
cool_reviewer.rate_hw(best_student_two, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Git', 1)
cool_reviewer.rate_hw(best_student_two, 'Git', 1)

# print(best_student.grades)
# print(cool_lecturer == cool_lecturer_two)
# print(cool_reviewer)
# print(cool_lecturer.grades)
# print(best_student_two)

lst_students = [best_student, best_student_two]
print(all_grade_students('Python', lst_students))

lst_lectors = [cool_lecturer, cool_lecturer_two]
print(all_grade_lectors('Python', lst_lectors))
