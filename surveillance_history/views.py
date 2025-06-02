from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import formset_factory
from surveillance.models import SurveillanceSession
from .models import SurveillanceHistory, PestDetection, DiseaseDetection
from .forms import SurveillanceHistoryForm, PestDetectionForm, DiseaseDetectionForm


@login_required
def record_result(request, session_id):
    """Record surveillance result"""
    session = get_object_or_404(SurveillanceSession, id=session_id, user=request.user)

    # Check if the surveillance session already has a result
    if SurveillanceHistory.objects.filter(session=session).exists():
        messages.warning(request, 'This surveillance session already has a result.')
        return redirect('session_detail', session_id=session.id)

    PestDetectionFormSet = formset_factory(PestDetectionForm, extra=3)
    DiseaseDetectionFormSet = formset_factory(DiseaseDetectionForm, extra=3)

    if request.method == 'POST':
        form = SurveillanceHistoryForm(request.POST)
        pest_formset = PestDetectionFormSet(request.POST, prefix='pests')
        disease_formset = DiseaseDetectionFormSet(request.POST, prefix='diseases')

        if form.is_valid() and pest_formset.is_valid() and disease_formset.is_valid():
            history = form.save(commit=False)
            history.session = session
            history.save()

            # Save pest and disease detection information
            for pest_form in pest_formset:
                if pest_form.is_valid() and pest_form.cleaned_data.get('pest_name') and pest_form.cleaned_data.get('count', 0) > 0:
                    pest = pest_form.save(commit=False)
                    pest.history = history
                    pest.save()

            for disease_form in disease_formset:
                if disease_form.is_valid() and disease_form.cleaned_data.get('disease_name') and disease_form.cleaned_data.get('count', 0) > 0:
                    disease = disease_form.save(commit=False)
                    disease.history = history
                    disease.save()

            session.plants_checked = history.plants_checked
            if session.plants_checked >= session.plants_to_check:
                session.status = 'completed'
            else:
                session.status = 'in_progress'
            session.save()

            messages.success(request, 'Surveillance result recorded successfully!')
            return redirect('history_detail', history_id=history.id)
    else:
        form = SurveillanceHistoryForm(initial={'plants_checked': session.plants_to_check})
        pest_formset = PestDetectionFormSet(prefix='pests')
        disease_formset = DiseaseDetectionFormSet(prefix='diseases')

    return render(request, 'surveillance_history/record_result.html', {
        'form': form,
        'pest_formset': pest_formset,
        'disease_formset': disease_formset,
        'session': session
    })


@login_required
def history_detail(request, history_id):
    """Display surveillance result details"""
    # Admin và viewer có thể xem tất cả dữ liệu lịch sử
    if hasattr(request.user, 'is_viewer_user') and request.user.is_viewer_user:
        # Người xem được xem tất cả history
        history = get_object_or_404(SurveillanceHistory, id=history_id)
    else:
        # Admin hoặc người dùng thường khác chỉ xem dữ liệu của mình
        history = get_object_or_404(SurveillanceHistory, id=history_id, session__user=request.user)
    return render(request, 'surveillance_history/history_detail.html', {'history': history})


@login_required
def history_list(request):
    """Display list of surveillance results"""
    # Admin và viewer có thể xem tất cả dữ liệu lịch sử
    if hasattr(request.user, 'is_viewer_user') and request.user.is_viewer_user:
        # Người xem được xem tất cả history
        histories = SurveillanceHistory.objects.all().order_by('-completion_date')
    else:
        # Admin hoặc người dùng thường khác chỉ xem dữ liệu của mình
        histories = SurveillanceHistory.objects.filter(session__user=request.user).order_by('-completion_date')
    return render(request, 'surveillance_history/history_list.html', {'histories': histories})
