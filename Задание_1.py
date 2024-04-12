class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = sum([sum(grades) for grades in self.grades.values()]) / \
            sum([len(grades) for grades in self.grades.values()])
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        my_avg_grade = sum([sum(grades) for grades in self.grades.values(
        )]) / sum([len(grades) for grades in self.grades.values()])
        other_avg_grade = sum([sum(other.grades[course]) for course in other.grades.keys(
        )]) / sum(len(other.grades[course]) for course in other.grades.keys())

        return my_avg_grade < other_avg_grade

    def __gt__(self, other):
        my_avg_grade = sum([sum(grades) for grades in self.grades.values(
        )]) / sum([len(grades) for grades in self.grades.values()])
        other_avg_grade = sum([sum(other.grades[course]) for course in other.grades.keys(
        )]) / sum(len(other.grades[course]) for course in other.grades.keys())

        return my_avg_grade > other_avg_grade


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
        avg_grade = sum([sum(grades) for grades in self.grades.values()]) / \
            sum([len(grades) for grades in self.grades.values()])
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}"

    def __lt__(self, other):
        my_avg_grade = sum([sum(grades) for grades in self.grades.values(
        )]) / sum([len(grades) for grades in self.grades.values()])
        other_avg_grade = sum([sum(other.grades[course]) for course in other.grades.keys(
        )]) / sum(len(other.grades[course]) for course in other.grades.keys())

        return my_avg_grade < other_avg_grade

    def __gt__(self, other):
        my_avg_grade = sum([sum(grades) for grades in self.grades.values(
        )]) / sum([len(grades) for grades in self.grades.values()])
        other_avg_grade = sum([sum(other.grades[course]) for course in other.grades.keys(
        )]) / sum(len(other.grades[course]) for course in other.grades.keys())

        return my_avg_grade > other_avg_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n Фамилия: {self.surname}"


student1 = Student("Alice", "Smith", "female")
student1.courses_in_progress = ["Math", "English"]
student1.finished_courses = ["History"]
student2 = Student("Bob", "Johnson", "male")
student2.courses_in_progress = ["Math", "History"]
student2.finished_courses = ["English"]

lecturer1 = Lecturer("John", "Doe")
lecturer1.courses_attached = ["Math", "English"]
lecturer2 = Lecturer("Emma", "Davis")
lecturer2.courses_attached = ["Math", "English"]

reviewer1 = Reviewer("Anna", "Wilson")
reviewer1.courses_attached = ["Math", "English"]
reviewer2 = Reviewer("Mark", "Brown")
reviewer2.courses_attached = ["History"]


reviewer1.rate_hw(student1, "Math", 5)
reviewer1.rate_hw(student2, "Math", 5)
reviewer1.rate_hw(student1, "English", 10)
reviewer1.rate_hw(student2, "English", 8)

student1.rate_lecture(lecturer1, "Math", 4)
student1.rate_lecture(lecturer2, "Math", 8)
student2.rate_lecture(lecturer1, "Math", 10)
student2.rate_lecture(lecturer2, "Math", 5)


print(student1)
print(student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)


def average_grade_per_course(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    if count != 0:
        return total / count
    else:
        return 0


def average_grade_per_lecture(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count != 0:
        return total / count
    else:
        return 0


print(average_grade_per_course([student1, student2], "Math"))
print(average_grade_per_lecture([lecturer1, lecturer2], "Math"))
