from django.contrib import admin
from .models import DailyPulses

# Register your models here.
@admin.register(DailyPulses)
class DailyPulsesAdmin(admin.ModelAdmin):
    list_display = ('user', 'energy_score', 'has_blocker', 'created_at')
    list_filter = ('has_blocker', 'energy_score', 'created_at')
    # Make the list searchable by the submitting user's email address
    search_fields = ('user__email', 'comment')