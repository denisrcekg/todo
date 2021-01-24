from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=100) #max lenght 100 symbols
    created_at = models.DateField(auto_now_add=True) # auto-insert date
    # created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False) # task is done = False
    is_favorite = models.BooleanField(default=False) # Task is not favorite by default
    
class Bookstore(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    is_in_store = models.BooleanField(default=True)

