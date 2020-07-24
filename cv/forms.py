from django import forms
from .models import CVPost

class CVForm(forms.ModelForm):

    class Meta:
        model = CVPost
        fields = ('profile', 'employment', 'education', 'skills', 'ecActivities', 'hobbies', 'references')