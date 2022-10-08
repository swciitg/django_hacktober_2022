from django.db import models

from rooms.models import Rooms
class Student(models.Model):

    Full_Name = models.TextField()
    Email = models.TextField(unique=True)
    Roll_Number = models.IntegerField(max_length=9)
    Student_No = models.IntegerField(primary_key=True)
    Temp_Permissions = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    Perm_Permissions = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    
    def _str_(self):
        return self.Student

class FutureBookings(models.Model):

    RoomNo = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    Student = models.TextField(Student, on_delete = models.CASCADE)
    Use = models.TextField()
    From = models.DateTimeField()
    Till = models.DateTimeField()
    
    def _str_(self):
        return self.FutureBookings