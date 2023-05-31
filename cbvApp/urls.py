from django.urls import path
from . import views

urlpatterns = [
    #path('', views.student_list),
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudnetDetail.as_view()),
]