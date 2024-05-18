from django.urls import path
from .import views 
from .views import TaskList, TaskDetail

urlpatterns = [
    path("", TaskList.as_view(), name= "tasklist"),
    path("task/<int:pk>", TaskDetail.as_view(), name= "taskdetails"),
    ##for testing purpose
    path("new", views.new, name= "new"),
    
]
