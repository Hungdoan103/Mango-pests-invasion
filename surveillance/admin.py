from django.contrib import admin
from .models import SurveillanceSession

@admin.register(SurveillanceSession)
class SurveillanceSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date', 'total_plants', 'plants_to_check', 'status', 'season')
    list_filter = ('status', 'date', 'season', 'user')
    search_fields = ('name', 'notes')
    readonly_fields = ('date', 'time', 'season', 'pest_alert_percentage', 'disease_alert_percentage')
    
    fieldsets = (
        (None, {
            'fields': ('name', 'user', 'total_plants', 'notes')
        }),
        ('Statistical Parameters', {
            'fields': ('confidence_level', 'error_margin', 'plants_to_check')
        }),
        ('Time Information', {
            'fields': ('date', 'time')
        }),
        ('Seasonal Alerts', {
            'fields': ('season', 'pest_alert_percentage', 'disease_alert_percentage')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )
