from django.db import models
from django.utils import timezone
from django.conf import settings
import math
import datetime
import pytz

class SurveillanceSession(models.Model):
    name = models.CharField(max_length=200, verbose_name="Session Name")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sessions')
    total_plants = models.IntegerField(verbose_name="Total Plants in Orchard")
    confidence_level = models.FloatField(default=0.95, verbose_name="Confidence Level (0-1)")
    error_margin = models.FloatField(default=0.05, verbose_name="Error Margin (0-1)")
    plants_to_check = models.IntegerField(verbose_name="Plants to Check")
    
    # Automatic timestamps
    date = models.DateField(auto_now_add=True, verbose_name="Survey Date")
    time = models.TimeField(auto_now_add=True, verbose_name="Survey Time")
    
    # Season and alerts (automatically determined from date in Darwin, Australia)
    SEASON_CHOICES = [
        ('wet_early', 'Early Wet Season (Nov-Dec)'),
        ('wet_peak', 'Peak Wet Season (Jan-Mar)'),
        ('dry_early', 'Early Dry Season (Apr-Jun)'),
        ('dry_peak', 'Peak Dry Season (Jul-Oct)'),
    ]
    season = models.CharField(max_length=20, choices=SEASON_CHOICES, verbose_name="Current Season")
    pest_alert_percentage = models.FloatField(verbose_name="Seasonal Pest Alert %")
    disease_alert_percentage = models.FloatField(verbose_name="Seasonal Disease Alert %")
    
    # Status
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, verbose_name="Notes")
    
    def save(self, *args, **kwargs):
        # Automatically calculate plants to check
        if not self.plants_to_check and self.total_plants:
            self.plants_to_check = self.calculate_sample_size()
        
        # Automatically determine season and alert rates based on current time
        if not self.id:  # Only automatically when creating new
            current_month = timezone.now().month
            self.season, self.pest_alert_percentage, self.disease_alert_percentage = self.get_current_season(current_month)
        
        super().save(*args, **kwargs)
    
    def calculate_sample_size(self):
        """Calculate plants to check based on Yamane formula"""
        # n = N / (1 + N*e²)
        denominator = 1 + self.total_plants * (self.error_margin ** 2)
        sample_size = self.total_plants / denominator
        return math.ceil(sample_size)  # Round up
    
    def get_current_season(self, month=None):
        """Determine season and pest/disease rates based on date in Darwin, Australia
        
        Darwin, Australia (12.4634° S, 130.8456° E) has two primary seasons:
        - Wet Season (November to April)
        - Dry Season (May to October)
        
        But for agricultural purposes, we'll use four seasons with specific pest/disease risk profiles:
        - Wet Season Early (Nov-Dec): High humidity, increasing rain
        - Wet Season Peak (Jan-Mar): Heavy rainfall, extreme humidity
        - Dry Season Early (Apr-Jun): Decreasing rainfall, moderate temperatures
        - Dry Season Peak (Jul-Oct): Minimal rainfall, lower temperatures
        """
        # If month is not provided, get current month in Darwin timezone
        if month is None:
            darwin_tz = pytz.timezone('Australia/Darwin')
            current_time = datetime.datetime.now(darwin_tz)
            month = current_time.month
        
        # Define seasons based on Darwin's climate patterns
        if month in [11, 12]:  # Wet Season Early
            return 'wet_early', 65.0, 35.0  # High pest risk, moderate disease risk
        elif month in [1, 2, 3]:  # Wet Season Peak
            return 'wet_peak', 75.0, 70.0   # Very high pest and disease risk
        elif month in [4, 5, 6]:  # Dry Season Early
            return 'dry_early', 50.0, 40.0  # Moderate pest and disease risk
        else:  # Dry Season Peak (7-10)
            return 'dry_peak', 30.0, 25.0   # Lower pest and disease risk
    
    def __str__(self):
        return f"Survey Session: {self.name} ({self.date})"
