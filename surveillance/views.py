from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SurveillanceSession
from .forms import SurveillanceSessionForm

@login_required
def dashboard(request):
    # Display dashboard with user's surveillance sessions
    sessions = SurveillanceSession.objects.filter(user=request.user).order_by('-date')
    return render(request, 'surveillance/dashboard.html', {'sessions': sessions})

@login_required
def create_session(request):
    if request.method == 'POST':
        form = SurveillanceSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            messages.success(request, 'New surveillance session created successfully!')
            return redirect('session_detail', session_id=session.id)
    else:
        form = SurveillanceSessionForm()
    return render(request, 'surveillance/create_session.html', {'form': form})

@login_required
def session_list(request):
    sessions = SurveillanceSession.objects.filter(user=request.user).order_by('-date')
    return render(request, 'surveillance/session_list.html', {'sessions': sessions})

@login_required
def session_detail(request, session_id):
    session = get_object_or_404(SurveillanceSession, id=session_id, user=request.user)
    return render(request, 'surveillance/session_detail.html', {'session': session})
