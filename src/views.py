from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required   #Ensures that a user must be authenticated to access a specific view
from .models import User
from .forms import CustomUserCreationForm
from django.http import HttpResponse


@login_required
def assign_role(request, user_id): #allows an Admin user to assign roles to other users
    if request.user.role != 'Admin':
        return render(request, 'users/permission_denied.html')

    user = User.objects.get(pk=user_id) #Retrieves the user by their id
    if request.method == 'POST':
         new_role = request.POST.get('role')
         if new_role in dict(User.ROLE_CHOICES):  # Validate role
             user.role = new_role
             user.save()
             messages.success(request, f"Role updated to {new_role} successfully.")
             return redirect('user_list')
         else:
             messages.error(request, "Invalid role selected.")

def user_list(request):
    users = User.objects.all() #Fetches all users from the database 
    return render(request, 'users/user_list.html', {'users': users})


    
def register_user(request): #handles new user registration
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def example_view(request): #Debugging placeholder to show user agent details
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse(f"Your user agent is: {user_agent}")



