from django.shortcuts import render

# Create your views here.
from .data import pests_list

def home(request):
    return render(request, 'app_project1/home.html')

def project_list(request):
    return render(request, 'app_project1/list.html', {'pests': pests_list})

def project_detail(request, item_id):
    item = next((x for x in pests_list if x.id == item_id), None)
    if not item:
        return render(request, '404.html', status=404)
    return render(request, 'app_project1/detail.html', {'item': item})

def about(request):
    team = [
        {'name': 'Umme Salma Rumana', 'id': 's367994'},
        {'name': 'Xuan Hung Doan', 'id': 's374988'},
        {'name': 'Trinh Nguyen', 'id': 's375352'},
        {'name': 'Melanie Bardoux', 'id': 's329560'},

        
    ]
    return render(request, 'app_project1/about.html', {'team': team})
