from django.db import models

# Create your models here.


class Instructor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Course(models.Model):
    name = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)#tell django that null is OK

    def __str__(self):
        return f'{self.name}: Instructor = {self.instructor}'

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f'ID: {self.id} OR {self.pk} NAME:{self.name} - {self.age} '


class MedicalRecord(models.Model):
    blood_type = models.CharField(max_length=4)
    student = models.OneToOneField(Student, on_delete=models.CASCADE) #cascade means this records will be deleted if a student is deleted

    def __str__(self):
        return f'{self.student.name}: Bloodt type: {self.blood_type}'

