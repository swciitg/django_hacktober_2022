from django.contrib import admin

# Register your models here.


# Register your models here.
from . models import Student
from . models import FutureBookings
admin.site.register(Student)
admin.site.register(FutureBookings)