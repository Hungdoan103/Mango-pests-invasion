from django.contrib import admin
from .models import SurveillanceHistory, PestDetection, DiseaseDetection

class PestDetectionInline(admin.TabularInline):
    model = PestDetection
    extra = 0

class DiseaseDetectionInline(admin.TabularInline):
    model = DiseaseDetection
    extra = 0

@admin.register(SurveillanceHistory)
class SurveillanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('session', 'completion_date', 'plants_checked', 'plants_with_pests', 
                    'plants_with_diseases', 'is_orchard_healthy')
    list_filter = ('is_orchard_healthy', 'completion_date', 'session__user')
    search_fields = ('session__name',)
    inlines = [PestDetectionInline, DiseaseDetectionInline]
    readonly_fields = ('completion_date', 'completion_time')
    
    fieldsets = (
        (None, {
            'fields': ('session', 'completion_date', 'completion_time')
        }),
        ('Survey Results', {
            'fields': ('plants_checked', 'plants_with_pests', 'plants_with_diseases')
        }),
        ('Conclusions', {
            'fields': ('is_orchard_healthy', 'recommendation')
        }),
    )
    
    def has_add_permission(self, request):
        # Do not allow adding directly from admin
        return False
