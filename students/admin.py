from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_no', 'course', 'age')
    list_filter = ('course',)
    search_fields = ('name', 'roll_no', 'course')
    ordering = ('name',)
