from django.db import models
from django.utils import timezone

class Blogs(models.Model):
    tech_stacks=[
        ('FRONTEND','FRONTEND'),
        ('BACKEND','BACKEND'),
        ('APP DEVELOPMENT','APP DEVELOPMENT'),
        ('MACHINE LEARNING','MACHINE LEARNING'),
        ('DJANGO','DJANGO'),
        ('REACTJS','REACTJS'),
        ('NODEJS','NODEJS'),
        ('FLUTTER','FLUTTER'),
        ('KOTLIN','KOTLIN'),
        ('PYTHON','PYTHON'),
        ('OTHERS','OTHERS')
    ]
    body=models.TextField(null=False)
    tech=models.CharField(choices=tech_stacks,null=True,blank=True,max_length=18)
    createdAt=models.DateTimeField(default=timezone.now)
