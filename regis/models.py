from django.db import models

class Category(models.Model):
    
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category
    
class Course(models.Model):

    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    credit = models.IntegerField()
    Semester = models.IntegerField()
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title  
