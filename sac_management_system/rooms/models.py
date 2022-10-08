from django.db import models

class Student(models.Model):
    pass


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
    Who_Has_Key_Currently = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    type = models.TextField(choices=Type.choices, default=Type.PUBLIC)

    def _str_(self):
        return self.Rooms


class LogEntry(models.Model):

    Room_No = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    Key_Taken = models.DateTimeField(null=True)
    Key_Given = models.DateTimeField()
    Student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    stage = models.TextField(choices=Stage.choices)

    def _str_(self):
        return self.LogEntry


class Student(models.Model):

    Full_Name = models.TextField()
    Email = models.TextField(unique=True)
    Roll_Number = models.IntegerField()
    Student_No = models.IntegerField(primary_key=True)
    Temp_Permissions = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    Perm_Permissions = models.ForeignKey(Rooms, on_delete=models.CASCADE)

    def _str_(self):
        return self.Student


class FutureBookings(models.Model):

    RoomNo = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Use = models.TextField()
    From = models.DateTimeField()
    Till = models.DateTimeField()

    def _str_(self):
        return self.FutureBookings


