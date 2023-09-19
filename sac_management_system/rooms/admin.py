from django.contrib import admin
from .models import Rooms, Student, LogEntry, FutureBookings

@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('Room_No', 'Room_Name', 'Room_Location', 'type')
    list_filter = ('type',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Full_Name', 'Email', 'phoneNumber', 'Roll_Number')
    search_fields = ('Full_Name', 'Email', 'Roll_Number')

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('Room_No', 'Student_ID', 'Key_Taken', 'Key_Given', 'stage')
    list_filter = ('stage',)

@admin.register(FutureBookings)
class FutureBookingsAdmin(admin.ModelAdmin):
    list_display = ('RoomNo', 'Student', 'Use', 'From', 'Till')
    list_filter = ('RoomNo', 'Student', 'Use')
