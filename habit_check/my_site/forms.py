from django import forms
from .models import Habits

class HabitCheckForm(forms.ModelForm):
    class Meta:
        model = Habits
        fields = ['is_checked_today']
        widgets = {
            'is_checked_today': forms.CheckboxInput(),
        }
