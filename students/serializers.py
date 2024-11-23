from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('roll_no', 'first_name', 'last_name' 'date_of_birth', 'gender', 'blood_group', 'contact_number', 'address', 'profile_picture')