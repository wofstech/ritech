from django.db import models
from django.conf import settings

class Profile(models.Model):  
    Student = 'S'
    Employed = 'E'
    Not_employed = 'N'
    Undergraduate = 'U'
    Others = 'O'
    User_type = (
        (Student, 'Student'),
        (Employed, 'Employed'),
        (Not_employed, 'Not employed'),
        (Undergraduate, 'Undergraduate'),
        (Others, 'Others'),
    ) 

    Male = 'Male'
    Female = 'Female'
    Gender = (
        (Male, 'Male'),
        (Female, 'Female'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)    
    date_of_birth = models.DateField(blank=True, null=True)
    City_of_residence = models.CharField(max_length=200)
    Type_of_user = models.CharField(max_length=40, choices=User_type, default=Student,)
    if_student = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField()
    phone_number = models.CharField(max_length=30)
    gender = models.CharField(max_length=40, choices=Gender, default=Male,)

    def __str__(self):        
        return 'Profile for user {}'.format(self.user.username)

class Houses(models.Model):
    Available = 'A'
    Not_Available = 'NA'
    Availability = (
        (Available, 'Available'),
        (Not_Available, 'Not_Available'),
    )
    name_of_accomodation = models.CharField(max_length=200)
    type_of_room = models.CharField(max_length=200)
    house_rent = models.IntegerField()
    availability = models.CharField(max_length=2, choices=Availability, default=Available,)
    location = models.CharField(max_length=200)
    nearest_institution = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_image')

    def __str__(self):
        return self.name_of_accomodation


class trial(models.Model):
    name = models.TextField()
    likes = models.TextField()

    def __str__(self):
        return self.name

class News(models.Model):
    email = models.EmailField()
    name = models.TextField()