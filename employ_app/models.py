from django.db import models

# Create your models here.


# class Blood_Groop(models.Model):
#     # Choices
#     BG = (
#          ('type', 'AB+'),
#         ('type', 'AB-'),
#         ('type', 'A+'),
#         ('type', 'A-'),
#         ('type', 'B+'),
#         ('type', 'B-'),
#         ('type', 'O+'),
#         ('type', 'O-'),
#     )


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name






class Role(models.Model):
    name=models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name=models.CharField(max_length=100)

    last_name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    blood_groop=models.CharField(max_length=4)
    dept=models.ForeignKey(
        'Department', on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
   
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey('Role',on_delete=models.CASCADE)
    medical_problem=models.TextField(max_length=3000)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.phone)
