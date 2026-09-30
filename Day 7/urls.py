from django.urls import path
from .views import task_api

urlpatterns = [
    path("tasks/", task_api, name="task_api"),
]