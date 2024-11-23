from rest_framework import serializers
from .models import Teachers

class TeachersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teachers
        fields = ('roll_no', 'first_name', 'last_name' 'date_of_birth', 'gender', 'blood_group', 'contact_number', 'address', 'profile_picture')