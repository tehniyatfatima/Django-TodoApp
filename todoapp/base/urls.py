from django.urls import path
from .import views 
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path("", TaskList.as_view(), name= "tasks"),
    path("task/<int:pk>", TaskDetail.as_view(), name= "task"),
    path("create/", TaskCreate.as_view(), name= "createtask"),
    path("updatetask/<int:pk>", TaskUpdate.as_view(), name= "updatetask"),
     path("deletetask/<int:pk>", TaskDelete.as_view(), name= "deletetask"),
    ##for testing purpose
    path("new", views.new, name= "new"),
    
]
