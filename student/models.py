from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, blank=False, null=True)
    current_address = models.CharField(max_length=100, null=True)