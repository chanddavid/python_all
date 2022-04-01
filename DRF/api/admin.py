from atexit import register
from multiprocessing.spawn import import_main_path
from operator import imod
from django.contrib import admin
from .models import Student

@admin.register(Student)

class StudentModelAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']