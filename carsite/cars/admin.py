from django.contrib import admin
from .models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    fields=['year','brand']

admin.site.register(Car,CarAdmin)