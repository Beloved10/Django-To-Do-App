from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
 
class Todo(models.Model):
    title=models.CharField(max_length=100) 
    date=models.DateTimeField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
 
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-date']