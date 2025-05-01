from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.crud_operations, name="crud"),
    path('delete/<int:id>/', views.delete_student_record, name="delete_data"),
    path('update/<int:id>/', views.update_student_record, name="update_data"),
]
