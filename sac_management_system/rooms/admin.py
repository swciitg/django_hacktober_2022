from django.contrib import admin

# Register your models here.



# Register your models here.
from .models import Rooms
from .models import LogEntry
admin.site.register(Rooms)
admin.site.register(LogEntry)