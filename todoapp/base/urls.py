from django.urls import path
from .import views 
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView

## for using direct logout functionality
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name= "login"),
    path("logout/", LogoutView.as_view(next_page ='login'), name= "logout"),
    path("", TaskList.as_view(), name= "tasks"),
    path("task/<int:pk>", TaskDetail.as_view(), name= "task"),
    path("create/", TaskCreate.as_view(), name= "createtask"),
    path("updatetask/<int:pk>", TaskUpdate.as_view(), name= "updatetask"),
     path("deletetask/<int:pk>", TaskDelete.as_view(), name= "deletetask"),
    ##for testing purpose
    path("new", views.new, name= "new"),
    
]
