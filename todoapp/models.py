from django.db import models


# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField()
    priority = models.TextField() 
    date1=models.DateField(auto_now_add=True)


#create your date models here.