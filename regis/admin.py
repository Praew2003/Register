from django.contrib import admin

# Register your models here.

from .models import Category, Course

@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = ("category",)
    search_fields = ("category",)
    
@admin.register(Course)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'credit','Semester','year','category',)
    