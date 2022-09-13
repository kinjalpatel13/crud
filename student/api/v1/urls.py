from django.urls import path, include
from student.api.v1 import views

urlpatterns = [
         path('', views.StudentAddApi.as_view(), name='index'),
         path('update/<int:pk>/', views.StudentUpdateApi.as_view(), name='update'),
         path('delete/<int:pk>/', views.StudentDeleteApi.as_view(), name='delete'),
         path('list/', views.StudentListApi.as_view(), name='list')
         
]                 