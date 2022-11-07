class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    pass
class Reviewer(Mentor):
    pass

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

mentor1 = Mentor('Some', 'Buddy')
mentor1.courses_attached += ['Python']

mentor1.rate_hw(best_student, 'Python', 10)
mentor1.rate_hw(best_student, 'Python', 10)
mentor1.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(f'Имя: {mentor1.name}\nФамилия: {mentor1.surname}\nЛекции: {mentor1.courses_attached}')