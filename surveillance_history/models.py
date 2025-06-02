from django.db import models
from surveillance.models import SurveillanceSession

class SurveillanceHistory(models.Model):
    session = models.ForeignKey(SurveillanceSession, on_delete=models.CASCADE, related_name='history')
    completion_date = models.DateField(auto_now_add=True, verbose_name="Completion Date")
    completion_time = models.TimeField(auto_now_add=True, verbose_name="Completion Time")
    
    # Survey results
    plants_checked = models.IntegerField(verbose_name="Plants Checked")
    plants_with_pests = models.IntegerField(default=0, verbose_name="Plants with Pests")
    plants_with_diseases = models.IntegerField(default=0, verbose_name="Plants with Diseases")
    
    # Conclusions
    is_orchard_healthy = models.BooleanField(default=True, verbose_name="Orchard is Healthy")
    recommendation = models.TextField(blank=True, verbose_name="Recommendation")
    
    def save(self, *args, **kwargs):
        season = self.session.season
        
        if season == 'wet_early':
            pest_threshold = 0.04
            disease_threshold = 0.03
            season_notes = "Early wet season brings increasing humidity and sporadic rainfall. Monitor for early signs of pests."
        elif season == 'wet_peak':
            pest_threshold = 0.03
            disease_threshold = 0.025
            season_notes = "Peak wet season has high humidity and heavy rainfall. Fungal diseases and insect pests are highly active."
        elif season == 'dry_early':
            pest_threshold = 0.05
            disease_threshold = 0.04
            season_notes = "Early dry season with decreasing rainfall. Some pests remain active while fungal diseases begin to decline."
        else:
            pest_threshold = 0.06
            disease_threshold = 0.05
            season_notes = "Peak dry season with minimal rainfall. Focus on drought stress and heat-tolerant pests."

        pest_percentage = self.plants_with_pests / self.plants_checked if self.plants_checked > 0 else 0
        disease_percentage = self.plants_with_diseases / self.plants_checked if self.plants_checked > 0 else 0

        season_treatments = {
            'wet_early': {
                'pest': "Use preventative sprays and increase monitoring frequency. Focus on early intervention.",
                'disease': "Apply preventative fungicides before heavy rains. Improve drainage in orchard."
            },
            'wet_peak': {
                'pest': "Implement intensive pest management with shorter intervals between treatments. Monitor daily if possible.",
                'disease': "Use systemic fungicides and ensure good air circulation. Remove infected materials immediately."
            },
            'dry_early': {
                'pest': "Transition to targeted pest control. Focus on remaining wet areas where pests concentrate.",
                'disease': "Continue monitoring but reduce fungicide applications as conditions dry."
            },
            'dry_peak': {
                'pest': "Focus on drought-tolerant pests. Monitor for unusual pest activity due to stress conditions.",
                'disease': "Minimal fungicide applications needed. Focus on preventing stress-related issues."
            }
        }

        if pest_percentage > pest_threshold or disease_percentage > disease_threshold:
            self.is_orchard_healthy = False

            if pest_percentage > pest_threshold and disease_percentage > disease_threshold:
                self.recommendation = (
                    f"Detected both pests ({pest_percentage:.1%}) and diseases ({disease_percentage:.1%}) during "
                    f"{self.session.get_season_display()}. {season_notes}\n\nRECOMMENDATIONS:\n"
                    f"- Pests: {season_treatments[season]['pest']}\n"
                    f"- Diseases: {season_treatments[season]['disease']}"
                )
            elif pest_percentage > pest_threshold:
                self.recommendation = (
                    f"Detected pests ({pest_percentage:.1%}) during {self.session.get_season_display()}. "
                    f"{season_notes}\n\nRECOMMENDATIONS:\n- {season_treatments[season]['pest']}"
                )
            else:
                self.recommendation = (
                    f"Detected diseases ({disease_percentage:.1%}) during {self.session.get_season_display()}. "
                    f"{season_notes}\n\nRECOMMENDATIONS:\n- {season_treatments[season]['disease']}"
                )
        else:
            self.is_orchard_healthy = True
            self.recommendation = (
                f"Orchard is healthy during {self.session.get_season_display()}. {season_notes}\n\nRECOMMENDATIONS:\n"
                f"Continue current management practices with seasonal adjustments for {self.session.get_season_display()}."
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Survey Result: {self.session.name} ({self.completion_date})"


class PestDetection(models.Model):
    history = models.ForeignKey(SurveillanceHistory, on_delete=models.CASCADE, related_name='pest_detections')
    pest_name = models.CharField(max_length=100, verbose_name="Pest Name")
    count = models.IntegerField(default=1, verbose_name="Count")
    severity = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='low')
    notes = models.TextField(blank=True, verbose_name="Notes")

    def __str__(self):
        return f"{self.pest_name} - {self.count} detected"


class DiseaseDetection(models.Model):
    history = models.ForeignKey(SurveillanceHistory, on_delete=models.CASCADE, related_name='disease_detections')
    disease_name = models.CharField(max_length=100, verbose_name="Disease Name")
    count = models.IntegerField(default=1, verbose_name="Count")
    severity = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='low')
    notes = models.TextField(blank=True, verbose_name="Notes")

    def __str__(self):
        return f"{self.disease_name} - {self.count} detected"
