
from student.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','student_id', 'first_name', 'last_name', 'phone_number', 'current_address']