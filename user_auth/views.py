from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Use authenticate with login credentials
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Login successful, welcome {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Unable to login with provided credentials. Please check and try again.')
        else:
            for error in form.non_field_errors():
                messages.error(request, f'{error}')
    else:
        form = LoginForm()
    return render(request, 'user_auth/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to dashboard in the surveillance application
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'user_auth/register.html', {'form': form})

def logout_view(request):
    # Clear all messages before logging out
    storage = messages.get_messages(request)
    # Process messages to display
    for message in storage:
        pass  # Read all messages
    # Mark all messages as used
    storage.used = True
    
    # Log out the user
    logout(request)
    
    # Add logout success message (optional)
    # messages.success(request, 'Logged out successfully!')
    
    return redirect('login')
