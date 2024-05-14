import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "django_intro_project.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW

from django_intro_app.models import *

# student = Student(name= 'J0hn Doe', age = 27)
# student.save()


# object_list = Student.objects.bulk_create(
#     [
#         Student(name='Bob Marley', age = 45),
#         Student(name='Albert Smith', age=55),
#         Student(name='Fred Flinstone', age=65)
#     ]

# )

# students = Student.objects.all()
# for student in students:
#     print(student)


# student = Student.objects.get(name='Bob Marley')

# print(student)


# students = Student.objects.filter(age__lt=30)
# for person in students:
#     print(person)

# student = Student.objects.filter(name='J0hn Doe').first()
# student.name = 'John Newname'
# student.save()



# Student.objects.filter(name='John Newname').first().delete()

# students = Student.objects.all()
# print(students)


# student = Student.objects.get(id=2)

# record = MedicalRecord(student=student, blood_type="A+")

# record.save()

# records = MedicalRecord.objects.all()
# print(records)

# Instructor.objects.bulk_create(
#     [
#         Instructor(name='Jeffrey Dalmer'),
#         Instructor(name='John Smith'),
#         Instructor(name='Blanchette Rosaline'),
#         Instructor(name='Jeff Ross'),
#         Instructor(name='Ashley Young')
#     ]
# )

# instructors= Instructor.objects.all()
# print(instructors)


# Course.objects.bulk_create(
#     [
#         Course(name='Python'),
#         Course(name='Intro to Psych'),
#         Course(name='Algebra'),
#         Course(name='French'),
#         Course(name='Procdural Programming')
#     ]
# )

# courses = Course.objects.all()
# print(courses)


# course = Course.objects.get(name='Python')
# course.instructor = Instructor.objects.get(name="John Smith")
# course.save()

# inst = Instructor.objects.get(name='Blanchette Rosaline')
# course = Course.objects.get(name='Algebra')
# course2 = Course.objects.get(name='French')
# #You can also use filter instead of get

# inst.course_set.add(course, course2)

# print(inst.name, inst.course_set.all())


python = Course.objects.get(name="Python")
procdural_programming = Course.objects.get(name="Procdural Programming")
psych = Course.objects.get(name="Intro to Psych")

students = Student.objects.all()

python.student_set.add(*students)
procdural_programming.student_set.add(*students)
psych.student_set.add(*students)


students = Student.objects.all()
for stu in students:
    print(stu.courses)