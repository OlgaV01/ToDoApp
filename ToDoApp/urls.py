from django.urls import path

from ToDoApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add_task"),
    path('update/<int:task_id>', views.update, name="update_task"),
    path('delete/<int:task_id>', views.delete, name="delete_task"),
    path('search/', views.search, name="search"),
]
