from modules.student import Student

student1 = Student("Ada", "E42")  # creates a new Student object
print(student1.student_name)
print(student1.student_cohort)

print(f"{student1.student_name} is in {student1.student_cohort}")  # Ada is in E42

print(student1.talk())  # I can talk!
print(student1.say_favourite_language("Python"))  # I love Python
