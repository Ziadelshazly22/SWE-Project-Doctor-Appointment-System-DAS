from django.urls import path
from . import views

urlpatterns = [
    path('assign_role/<int:user_id>/', views.assign_role, name='assign_role'), #Allows an Admin to assign a role
    path('example/', views.example_view, name='example'),  # Example route
    path('user_list/', views.user_list, name='user_list'), #Displays a list of all users.
]
print("users/urls.py is being loaded")



