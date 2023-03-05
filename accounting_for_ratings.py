class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_score = 0

    def evaluation_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'         
    
    def __str__(self):
        grades_quality = 0
        grades_sum = 0
        for key, value in self.grades.items():
            for _ in value:
                grades_quality += 1
                grades_sum += _
        self.average_score = (grades_sum / grades_quality)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_score}\n'
                f'Курсы в процессе изучения: {"{[0]}".format([", ".join(i for i in self.courses_in_progress)])}\n'
                f'Завершенные курсы: {"{[0]}".format([", ".join(i for i in self.finished_courses)])}')

    def grades_homework_course(list_, course):
        grades_quality = 0
        grades_sum = 0
        for student_ in list_:
            if course in student_.courses_in_progress and isinstance(student_, Student):
                for key, value in student_.grades.items():
                    if key == course:
                        for _ in value:
                            grades_quality += 1
                            grades_sum += _
                x = (grades_sum / grades_quality)
        return f'Средняя оценка студентов на курсе {course}: {x}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет студента')
            return
        return self.average_score < other.average_score
    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] 


class Lecturer(Mentor):
    """
    лекторы
    """
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.average_score = 0
        
    def __str__(self):
        grades_quality = 0
        grades_sum = 0
        for key, value in self.grades.items():
            for _ in value:
                grades_quality += 1
                grades_sum += _
        self.average_score = (grades_sum / grades_quality)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_score}')    

    def grades_lectures_course(list_, course):
        grades_quality = 0
        grades_sum = 0
        for teacher in list_:
            if course in teacher.courses_attached and isinstance(teacher, Lecturer):
                for key, value in teacher.grades.items():
                    if key == course:
                        for _ in value:
                            grades_quality += 1
                            grades_sum += _
                x = (grades_sum / grades_quality)
        return f'Средняя оценка лекторов на курсе {course}: {x}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет лектора')
            return
        return self.average_score < other.average_score


class Reviewer(Mentor):
    """
    эксперты, проверяющие домашние задания
    """
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        
    def evaluation_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

list_student = []    
list_lecturer = []
    
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
list_student.append(some_student)
another_some_student = Student('Thomas', 'Phelps', 'your_gender')
another_some_student.courses_in_progress += ['JavaScript', 'Git']
another_some_student.finished_courses += ['Введение в программирование', 'SQL']
list_student.append(another_some_student)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']
another_some_reviewer = Reviewer('Todd', 'Stevenson')
another_some_reviewer.courses_attached += ['Python', 'JavaScript', 'SQL']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Git']
list_lecturer.append(some_lecturer)
another_some_lecturer = Lecturer('Todd', 'Stevenson')
another_some_lecturer.courses_attached += ['Python', 'JavaScript', 'SQL']
list_lecturer.append(another_some_lecturer)

some_reviewer.evaluation_student(some_student, 'Python', 10)
some_reviewer.evaluation_student(some_student, 'Python', 7)
some_reviewer.evaluation_student(some_student, 'Git', 10)
some_reviewer.evaluation_student(some_student, 'Git', 9)
some_reviewer.evaluation_student(another_some_student, 'Git', 10)
some_reviewer.evaluation_student(another_some_student, 'Git', 9)
another_some_reviewer.evaluation_student(some_student, 'Python', 10)
another_some_reviewer.evaluation_student(another_some_student, 'JavaScript', 10)
another_some_reviewer.evaluation_student(another_some_student, 'JavaScript', 9)

some_student.evaluation_lecturer(some_lecturer, 'Python', 7)
some_student.evaluation_lecturer(some_lecturer, 'Python', 10)
some_student.evaluation_lecturer(another_some_lecturer, 'Python', 10)
some_student.evaluation_lecturer(another_some_lecturer, 'Python', 9)
some_student.evaluation_lecturer(some_lecturer, 'Git', 9)
some_student.evaluation_lecturer(some_lecturer, 'Git', 9)
another_some_student.evaluation_lecturer(another_some_lecturer, 'JavaScript', 7)
another_some_student.evaluation_lecturer(another_some_lecturer, 'JavaScript', 8)
another_some_student.evaluation_lecturer(some_lecturer, 'Git', 9)

print(f'{some_reviewer}\n\n{some_lecturer}\n\n{some_student}', end='\n\n')
print(f'{another_some_reviewer}\n\n{another_some_lecturer}\n\n{another_some_student}', end='\n\n')
print(some_lecturer < another_some_lecturer)
print(some_student < another_some_student, end='\n\n')
print(Lecturer.grades_lectures_course(list_lecturer, 'JavaScript'))
print(Student.grades_homework_course(list_student, 'Python'))