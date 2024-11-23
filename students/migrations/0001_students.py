from django.db import migrations

def create_data(apps, schema_editor):
    Student = apps.get_model('students','Student')
    Student(first_name="Hinata", last_name="Hyuga", date_of_birth="2002/05/12", gender="1", blood_group="B+", contact_number="9988776655", address="Home, Hyuga Estate, Japan").save()

class Migration(migrations.Migration):

    dependencies = [
            ('students', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_data)
    ]
