from django.db import models
from django.conf import settings


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=64);
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title

class Task(models.Model):
    TASK_STATUS = [
        ('W', 'Wating'),
        ('P', 'In Progress'),
        ('C', 'Complete')
    ]
    
    PRIORITY = [
        ('H', 'HIGH'),
        ('M', 'MEDIUM'),
        ('L', 'LOW'),
    ]

    user =          models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title =         models.CharField(max_length=64)
    category =      models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='tasks', blank=True)
    description =   models.TextField(max_length=256)
    has_reminder =  models.BooleanField(default=False)
    reminder =      models.DateTimeField()
    status =        models.CharField(max_length=2, choices=TASK_STATUS)
    color =         models.CharField(max_length=8, default="#000000")#  The color of the task in Hex format
    proirity =      models.CharField(max_length=2, choices=PRIORITY)