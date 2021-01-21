from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=100) #mal lenght 100 symbols
    created_at = models.DateField(auto_now_add=True) # auto-insert date-time
    is_closed = models.BooleanField(default=False) # task is done = False
    is_favorite = models.BooleanField(default=False) # Task is not favorite by default
    

