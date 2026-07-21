from django.db import models
from django.contrib.auth.models import User

class DailyInput(models.Model):
    MOOD_CHOICES = [
        ('very_bad', 'Very Bad'),
        ('bad', 'Bad'),
        ('neutral', 'Neutral'),
        ('good', 'Good'),
        ('very_good', 'Very Good'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    sleep_duration = models.FloatField(help_text="Hours of sleep")
    workload = models.IntegerField(help_text="Workload level 1-10")
    notes = models.TextField(blank=True, null=True)
    stress_level = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"
    
    def calculate_stress_level(self):
        """Calculate stress score based on inputs"""
        stress = 0
        
        # Mood impact (0-4)
        mood_map = {'very_bad': 4, 'bad': 3, 'neutral': 2, 'good': 1, 'very_good': 0}
        stress += mood_map.get(self.mood, 2)
        
        # Sleep impact (0-3)
        if self.sleep_duration < 6:
            stress += 3
        elif self.sleep_duration < 7:
            stress += 2
        elif self.sleep_duration < 8:
            stress += 1
        
        # Workload impact (0-3)
        if self.workload >= 8:
            stress += 3
        elif self.workload >= 6:
            stress += 2
        elif self.workload >= 4:
            stress += 1
        
        self.stress_level = stress
        return stress
    
    def save(self, *args, **kwargs):
        self.calculate_stress_level()
        super().save(*args, **kwargs)