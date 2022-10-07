from django.db import models


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
    Room_No = models.IntegerField()
    Room_Details = models.TextField()
    Who_Has_Key_Currently = models.IntegerField()
    type = models.TextField(choices=Type.choices, default=Type.PUBLIC)

    def _str_(self):
        return self.Rooms


class LogEntry(models.Model):

    Room_No = models.IntegerField()
    Key_Taken = models.DateTimeField()
    Key_Given = models.DateTimeField()
    Student_ID = models.TextField()
    stage = models.TextField(choices=Stage.choices)

    def _str_(self):
        return self.LogEntry
