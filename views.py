from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re
from .models.pest import Pest
from .models.disease import Disease
from .enums.pest_enums import Category, Severity, Type, TypeDetail, AffectedPart, Season
from .data.mango_data import pest_disease_data
from app_project1.data import pests_list

# Create your views here.

def get_enum_value(enum_obj):
    """Helper function to get the actual value from an enum object"""
    if isinstance(enum_obj, (Category, Severity, Type, TypeDetail, AffectedPart, Season)):
        return enum_obj.value
    return enum_obj

def sanitize_regex(query):
    """Sanitize the search query for regex safety"""
    return re.escape(query)

@login_required
def pest_disease_list(request):
    try:
        search_query = request.GET.get('search', '').strip()
        type_filter = request.GET.get('type', '').strip()
        name_sort = request.GET.get('name_sort', '').strip()

        # Get the first 7 pests from mango_data
        pests_data = [item for item in pest_disease_data if item.get('category') == Category.PEST][:7]
        
        # Update or create Pest objects
        for pest_data in pests_data:
            try:
                # Convert enum objects to their string values
                defaults = {
                    'name': pest_data.get('name', ''),
                    'category': get_enum_value(pest_data.get('category')),
                    'severity': get_enum_value(pest_data.get('severity')),
                    'type': get_enum_value(pest_data.get('type')),
                    'type_detail': get_enum_value(pest_data.get('type_detail')),
                    'season': pest_data.get('season', ''),
                    'sci_name': pest_data.get('sci_name', ''),
                    'affected_part': pest_data.get('affected_part', ''),
                    'egg': pest_data.get('egg', ''),
                    'larvae': pest_data.get('larvae', ''),
                    'adult': pest_data.get('adult', ''),
                    'long_desc': pest_data.get('long_desc', ''),
                    'life_cycle': pest_data.get('life_cycle', ''),
                    'symptoms': pest_data.get('symptoms', ''),
                    'damage': pest_data.get('damage', ''),
                    'monitoring': pest_data.get('monitoring', ''),
                    'intervention': pest_data.get('intervention', ''),
                    'control_measures': pest_data.get('control_measures', ''),
                    'ref': pest_data.get('ref', '')
                }

                # Update or create pest object
                pest_obj, created = Pest.objects.update_or_create(
                    item_id=pest_data.get('item_id'),
                    defaults=defaults
                )
                if created:
                    print(f"Created new pest: {pest_obj.name}")
                else:
                    print(f"Updated existing pest: {pest_obj.name}")

            except Exception as e:
                print(f"Error processing pest {pest_data.get('name', 'Unknown')}: {str(e)}")
                print(f"Full error: {str(e.__class__.__name__)}: {str(e)}")

        # Initialize querysets
        pests = Pest.objects.all().order_by('item_id')[:7]
        diseases = Disease.objects.all()

        # Apply search if query exists
        if search_query:
            safe_query = sanitize_regex(search_query)
            pests = pests.filter(
                Q(name__iregex=safe_query) |
                Q(type__iregex=safe_query) |
                Q(type_detail__iregex=safe_query) |
                Q(long_desc__iregex=safe_query) |
                Q(affected_part__iregex=safe_query) |
                Q(season__iregex=safe_query)
            )
            diseases = diseases.filter(
                Q(name__iregex=safe_query) |
                Q(type__iregex=safe_query) |
                Q(short_desc__iregex=safe_query) |
                Q(affected_part__iregex=safe_query) |
                Q(season__iregex=safe_query)
            )

        # Apply type filter
        if type_filter:
            pests = pests.filter(type=type_filter)
            diseases = diseases.filter(type=type_filter)

        # Apply name sorting
        if name_sort:
            order_by = 'name' if name_sort == 'asc' else '-name'
            pests = pests.order_by(order_by)
            diseases = diseases.order_by(order_by)

        # Print debug information
        print(f"Number of pests being sent to template: {pests.count()}")
        for pest in pests:
            print(f"Pest: {pest.name}, ID: {pest.item_id}")

        context = {
            'pests': pests,
            'diseases': diseases,
            'search_query': search_query,
            'type_filter': type_filter,
            'name_sort': name_sort
        }
        return render(request, 'pest_disease/list.html', context)

    except ImportError as e:
        print(f"Error importing mango_data: {str(e)}")
        return render(request, 'pest_disease/list.html', {'pests': [], 'diseases': []})
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return render(request, 'pest_disease/list.html', {'pests': [], 'diseases': []})

@login_required
def convert_id_to_app_project1_format(item_id):
    """Chuyển đổi ID từ format 1-14 sang format P01/D01"""
    try:
        id_num = int(item_id)
        # Mapping các ID từ database sang ID trong app_project1
        id_mapping = {
            1: "P01",  # Mango Seed Weevil
            2: "P02",  # Fruitspotting Bug
            3: "P03",  # Fruit Flies
            4: "P04",  # Mango Leafhopper
            5: "P05",  # Mango Fruit Borer
            6: "P06",  # Redbanded Thrips
            7: "P07",  # Tea Mosquito Bug
            8: "D03",  # Mango Malformation Disease
            9: "D01",  # Algal Leaf Spot
            10: "D02",  # Stem End Rot
            11: "D04",  # Bacterial Black Spot
            12: "D05",  # Pink Disease
            13: "D06",  # Anthracnose
            14: "D07"   # Powdery Mildew
        }
        return id_mapping.get(id_num)
    except ValueError:
        return None

@login_required
def pest_disease_detail(request, item_id):
    try:
        print(f"Looking for item_id: {item_id}")
        
        # Chuyển đổi ID sang format của app_project1
        app_project1_id = convert_id_to_app_project1_format(item_id)
        if not app_project1_id:
            print("Invalid ID format")
            return render(request, '404.html', status=404)
            
        # Redirect đến trang detail của app_project1 sử dụng reverse URL
        detail_url = reverse('project_detail', args=[app_project1_id])
        return redirect(detail_url)
        
    except Exception as e:
        print(f"Error in pest_disease_detail: {str(e)}")
        return render(request, '404.html', status=404)
