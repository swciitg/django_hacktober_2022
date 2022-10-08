from django.contrib import admin
from .models import Rooms, LogEntry, Student, FutureBookings

admin.site.register(Rooms)
admin.site.register(LogEntry)
admin.site.register(Student)
admin.site.register(FutureBookings)
