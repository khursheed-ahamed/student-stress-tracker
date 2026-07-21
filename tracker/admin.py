from django.contrib import admin
from .models import DailyInput

@admin.register(DailyInput)
class DailyInputAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'mood', 'sleep_duration', 'workload', 'stress_level')
    list_filter = ('date', 'mood')
    search_fields = ('user__username',)
    readonly_fields = ('stress_level', 'date')