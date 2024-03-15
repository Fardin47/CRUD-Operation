from django.db import models

# Create your models here.
# Need to inherit this model class in order to have the Django ORM or model features.
# For any model there will be a primary key that will be automatically created by Django ORM.


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    empcode = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE
    )  # Whenever we delete a record from this position table emp table record will be auto deleted [on_delete=models.CASCADE]


# python manage.py sqlmigrate employee_register 0001 --> Corresponding SQL command to apply those modifications.
# python manage.py migrate --> In order to execute the SQL Script need to execute this command.
