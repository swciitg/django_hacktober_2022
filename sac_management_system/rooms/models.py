from django.db import models
from django.core.validators import RegexValidator

# from .models import Student

class Type(models.TextChoices):
    PUBLIC = 'Public',
    CLUB = 'Club',


class Stage(models.TextChoices):
    RETURNED = 'Returned',
    TAKEN = 'Taken',
    REQUESTED = 'Requested',


class Rooms(models.Model):

    Room_Name = models.TextField()
    Room_Location = models.TextField()
    Room_No = models.IntegerField(primary_key=True)
    Room_Details = models.TextField(null=True)
    Who_Has_Key_Currently = models.TextField(null=True)
    type = models.TextField(choices=Type.choices, default=Type.PUBLIC)

    def _str_(self):
        return self.Rooms
class Student(models.Model):

    Full_Name = models.TextField()
    Email = models.EmailField(unique=True, max_length=254)
    phoneNumberRegex = RegexValidator(regex=r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=13, unique=True)
    Roll_Number = models.CharField(max_length=9)
    Student_No = models.IntegerField(primary_key=True)
    Temp_Permissions = models.IntegerField()
    Perm_Permissions = models.IntegerField()

    def _str_(self):
        return self.Student


class LogEntry(models.Model):

    Room_No = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    Key_Taken = models.DateTimeField(auto_now_add=True, blank=False)
    Key_Given = models.DateTimeField()
    Student_ID = models.ForeignKey(Student, on_delete = models.CASCADE)
    stage = models.TextField(choices=Stage.choices, default = Stage.RETURNED)

    def _str_(self):
        return self.LogEntry

class FutureBookings(models.Model):

    RoomNo = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    Student = models.ForeignKey(Student, on_delete = models.CASCADE)
    Use = models.TextField()
    From = models.DateTimeField()
    Till = models.DateTimeField()

    def _str_(self):
        return self.FutureBookings


