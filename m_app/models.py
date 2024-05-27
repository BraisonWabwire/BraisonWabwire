from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    course=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    

    def __str__(self):
        return self.name
    

class studSignup(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    d_o_b=models.DateField()
    id_number=models.IntegerField()
    email=models.EmailField(max_length=50)
    course=models.CharField(max_length=30)

    def __str__(self):
        return self.f_name


class StudentFile(models.Model):
    # student_Fname = models.ForeignKey(studSignup, on_delete=models.CASCADE)
    # student_Lname=models.ForeignKey(studSignup, on_delete=models.CASCADE)
    emial=models.EmailField(max_length=50)
    certificate=models.FileField()
    # Additional fields for StudentFile can be added here

    def __str__(self):
        return self.emial



