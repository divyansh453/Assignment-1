from rest_framework import serializers
from .models import *
from django.contrib.postgres.fields import ArrayField

class BlogCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model=Blogs
        fields=['id','body','tech']
class BlogViewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Blogs
        fields=['id','body','tech','createdAt']

