Merna
from django.urls import path
from . import views

urlpatterns = [
    path('assign_role/<int:user_id>/', views.assign_role, name='assign_role'), #Allows an Admin to assign a role
    path('example/', views.example_view, name='example'),  # Example route
    path('user_list/', views.user_list, name='user_list'), #Displays a list of all users.
]
print("users/urls.py is being loaded")
"""
URL configuration for BackendProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
main
