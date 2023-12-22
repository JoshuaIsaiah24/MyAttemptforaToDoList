from django.db import models

# Create your models here.

class ToDo(models.Model):
    task = models.CharField(max_length=100)
    complete = models.BooleanField(null=True)
    
    def __str__(self) -> str:
        return self.task
