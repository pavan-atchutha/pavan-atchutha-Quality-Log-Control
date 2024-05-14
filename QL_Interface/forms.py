from django import forms
from .models import LogEntry

class LogForm(forms.ModelForm):
    class Meta:
        model = LogEntry
        fields = ['level', 'log_string','timestamp', 'metadata_source']

class LogFilterForm(forms.Form):
    level = forms.ChoiceField(choices=[('', 'All'), ('DEBUG', 'Debug'), ('INFO', 'Info'), ('WARNING', 'Warning'), ('ERROR', 'Error'), ('CRITICAL', 'Critical')], required=False)
    log_string = forms.CharField(required=False)
    timestamp = forms.DateTimeField(required=False) #widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    metadata_source = forms.CharField(widget=forms.Textarea,required=False)
