import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import DailyInput
from .forms import DailyInputForm, SignUpForm

def get_stress_category(stress_level):
    """Categorize stress level into low, medium, or high"""
    if stress_level <= 3:
        return 'Low'
    elif stress_level <= 6:
        return 'Medium'
    else:
        return 'High'

def get_suggestions(stress_level):
    """Get suggestions based on stress level"""
    stress_level = int(stress_level)
    
    if stress_level <= 3:
        return [
            '✓ Keep up the great work! Your stress levels are healthy.',
            '✓ Continue with your regular exercise routine.',
            '✓ Maintain a balanced sleep schedule.',
            '✓ Engage in relaxing activities you enjoy.',
        ]
    elif stress_level <= 6:
        return [
            '⚠ Your stress is moderate. Try these tips:',
            '• Take short breaks during work/study sessions.',
            '• Practice deep breathing exercises.',
            '• Limit caffeine intake.',
            '• Spend time with friends or family.',
            '• Try meditation or yoga.',
        ]
    else:
        return [
            '⚠ Your stress levels are high. Please try:',
            '• Take regular breaks - step away from work.',
            '• Practice mindfulness or meditation.',
            '• Get adequate sleep (7-8 hours).',
            '• Exercise regularly for stress relief.',
            '• Talk to friends, family, or a counselor.',
            '• Avoid excessive caffeine and sugar.',
        ]

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    stress_logs = DailyInput.objects.filter(user=request.user).order_by('-date')[:7]
    stress_labels = [str(log.date) for log in reversed(stress_logs)]
    stress_values = [log.stress_level for log in reversed(stress_logs)]
    
    # Get the latest stress log
    latest_log = stress_logs.first() if stress_logs else None
    current_stress_level = latest_log.stress_level if latest_log else 0
    stress_category = get_stress_category(current_stress_level)
    suggestions = get_suggestions(current_stress_level)
    
    # Determine color based on stress category
    if stress_category == 'Low':
        stress_color = 'success'  # Green
    elif stress_category == 'Medium':
        stress_color = 'warning'  # Yellow
    else:
        stress_color = 'danger'   # Red
    
    context = {
        'stress_logs': stress_logs,
        'stress_labels': json.dumps(stress_labels),
        'stress_values': json.dumps(stress_values),
        'current_stress_level': current_stress_level,
        'stress_category': stress_category,
        'stress_color': stress_color,
        'suggestions': suggestions,
    }
    return render(request, 'dashboard.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def stress_log(request):
    if request.method == 'POST':
        form = DailyInputForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            return redirect('dashboard')
    else:
        form = DailyInputForm()
    return render(request, 'stress_log.html', {'form': form})

@login_required
def analytics(request):
    # Get all stress logs for the user
    stress_logs = DailyInput.objects.filter(user=request.user).order_by('-date')[:30]
    
    if stress_logs:
        stress_labels = [str(log.date) for log in reversed(stress_logs)]
        stress_values = [log.stress_level for log in reversed(stress_logs)]
        
        # Calculate statistics
        avg_stress = sum(stress_values) / len(stress_values)
        max_stress = max(stress_values)
        min_stress = min(stress_values)
        
        # Categorize stress levels
        low_count = len([s for s in stress_values if s <= 3])
        medium_count = len([s for s in stress_values if 4 <= s <= 6])
        high_count = len([s for s in stress_values if s > 6])
    else:
        stress_labels = []
        stress_values = []
        avg_stress = 0
        max_stress = 0
        min_stress = 0
        low_count = 0
        medium_count = 0
        high_count = 0
    
    context = {
        'stress_labels': json.dumps(stress_labels),
        'stress_values': json.dumps(stress_values),
        'avg_stress': round(avg_stress, 2),
        'max_stress': max_stress,
        'min_stress': min_stress,
        'low_count': low_count,
        'medium_count': medium_count,
        'high_count': high_count,
        'total_logs': len(stress_values),
    }
    return render(request, 'analytics.html', context)

@login_required
def resources(request):
    resources_data = {
        'stress_relief': [
            {'title': 'Deep Breathing Exercises', 'description': 'Practice 4-7-8 breathing to calm your nervous system', 'tip': '4 count in, 7 hold, 8 count out'},
            {'title': 'Meditation', 'description': 'Clear your mind and focus on the present moment', 'tip': 'Start with 5-10 minutes daily'},
            {'title': 'Journaling', 'description': 'Write down your thoughts and emotions', 'tip': 'Spend 10-15 minutes daily reflecting'},
        ],
        'exercise': [
            {'title': 'Walking', 'description': 'Simple and effective way to reduce stress', 'tip': '30 minutes daily at moderate pace'},
            {'title': 'Yoga', 'description': 'Combine stretching, breathing, and mindfulness', 'tip': 'Try beginner-friendly classes on YouTube'},
            {'title': 'Running', 'description': 'High-intensity cardio for endorphin release', 'tip': '3-4 times weekly for best results'},
        ],
        'sleep': [
            {'title': 'Consistent Sleep Schedule', 'description': 'Go to bed and wake at the same time daily', 'tip': 'Aim for 7-9 hours of sleep'},
            {'title': 'Sleep Environment', 'description': 'Keep bedroom dark, cool, and quiet', 'tip': 'Temperature around 65-68°F is ideal'},
            {'title': 'Avoid Screens Before Bed', 'description': 'Put away phones and laptops 1 hour before sleep', 'tip': 'Blue light disrupts melatonin production'},
        ],
        'apps': [
            {'title': 'Headspace', 'description': 'Meditation and mindfulness app with guided sessions', 'link': 'headspace.com'},
            {'title': 'Calm', 'description': 'Sleep stories, meditation, and breathing exercises', 'link': 'calm.com'},
            {'title': 'Insight Timer', 'description': 'Free meditation app with thousands of sessions', 'link': 'insighttimer.com'},
        ],
        'professional': [
            {'title': 'Therapist/Counselor', 'description': 'Professional mental health support', 'tip': 'Consider therapy for ongoing stress'},
            {'title': 'Support Groups', 'description': 'Connect with others experiencing similar stress', 'tip': 'Find local or online support communities'},
            {'title': 'Doctor Consultation', 'description': 'Medical evaluation for stress-related issues', 'tip': 'Rule out medical causes of stress'},
        ]
    }
    
    context = {'resources_data': resources_data}
    return render(request, 'resources.html', context)