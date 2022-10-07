from django.db import models

class Student(models.Model):

    Full_Name = models.TextField()
    Email = models.TextField()
    Roll_Number = models.IntegerField()
    Student_No = models.IntegerField()
    Temp_Permissions = models.IntegerField()
    Perm_Permissions = models.IntegerField()
    
    def _str_(self):
        return self.Student

class FutureBookings(models.Model):

    RoomNo = models.IntegerField()
    Student = models.IntegerField()
    Use = models.TextField()
    From = models.DateTimeField()
    Till = models.DateTimeField()
    
    def _str_(self):
        return self.FutureBookings