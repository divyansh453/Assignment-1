from django.db import models
from django.utils import timezone

class Blogs(models.Model):
    body=models.TextField(null=False)
    tech=models.CharField(null=True,blank=True,max_length=18)
    createdAt=models.DateTimeField(default=timezone.now)
