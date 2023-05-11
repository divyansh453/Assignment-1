from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView,GenericAPIView
from .serializers import *
from .models import *

class BlogCreateView(GenericAPIView):
    serializer_class=BlogCreateSerializers
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET'])
def BlogList(request):
    blog=Blogs.objects.all()
    blogs_=BlogViewSerializers(blog,many=True)
        
    return Response(blogs_.data)
class BlogRUD(RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogCreateSerializers

