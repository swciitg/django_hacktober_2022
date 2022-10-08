from django.db import models

from student.models import Student

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
    Who_Has_Key_Currently = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    type = models.TextField(choices=Type.choices, default=Type.PUBLIC)

    def _str_(self):
        return self.Rooms


class LogEntry(models.Model):

    Room_No = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    Key_Taken = models.DateTimeField(null=True)
    Key_Given = models.DateTimeField()
    Student_ID = models.IntegerField(Student, on_delete = models.CASCADE)
    stage = models.TextField(choices=Stage.choices)

    def _str_(self):
        return self.LogEntry



