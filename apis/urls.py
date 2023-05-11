from django.urls import path
from .views import *

urlpatterns = [
    path('blog_create/',BlogCreateView.as_view()),
    path('blog_RUD/<int:pk>',BlogRUD.as_view()),
    path('blog_list/',BlogList),
 
]

