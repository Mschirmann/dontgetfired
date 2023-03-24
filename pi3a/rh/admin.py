from django.contrib import admin
from .models import Time_sheet, Vacations, Holidays

# Register your models here.
admin.site.register(Time_sheet)
admin.site.register(Vacations)
admin.site.register(Holidays)
# admin.site.register(NewUser)
