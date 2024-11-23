from django.db import models

# Create your models here.
class Teachers(models.Model):
    id = models.IntegerField("ID", primary_key=True, serialize=True)
    first_name = models.CharField("First Name", max_length=240)
    last_name = models.CharField("Last Name", max_length=240)
    date_of_birth = models.DateField("Date of Birth")
    gender = models.IntegerField("Gender")
    blood_group = models.CharField("Blood Group", max_length=7)
    contact_number = models.CharField("Contact Number", max_length=15)
    address = models.TextField("Address")
    profile_picture = models.ImageField("Profile Picture", upload_to='files/profile/')

