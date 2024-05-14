# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .forms import LogForm, LogFilterForm
from .models import LogEntry
import json

def home(request):
    return render(request, 'home.html')

def send_log(request):
    if request.method == 'POST':
        log_form = LogForm(request.POST)
        if log_form.is_valid():
            log_form.save()
            return JsonResponse({'message': 'Log entry created successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Invalid data in log form'}, status=400)
    else:
        log_form = LogForm()
    return render(request, 'send_log.html', {'log_form': log_form})

def filter_logs(request):
    if request.method == 'POST':
        log_filter_form = LogFilterForm(request.POST)
        if log_filter_form.is_valid():
            level = log_filter_form.cleaned_data.get('level')
            log_string = log_filter_form.cleaned_data.get('log_string')
            metadata_source = log_filter_form.cleaned_data.get('metadata_source')
            timestamp = log_filter_form.cleaned_data.get('timestamp')
            # print(level,metadata_source,timestamp)
            try:
                metadata_source = json.loads(metadata_source)  # Convert string to JSON object
            except json.JSONDecodeError:
                # Handle JSON decoding error
                # You can add error handling logic here
                pass

            queryset = LogEntry.objects.all()
            # print(queryset)
            if level:
                queryset = queryset.filter(level=level)
                # print(1,queryset)
            if log_string:
                queryset = queryset.filter(log_string=log_string)
            if metadata_source:
                queryset = queryset.filter(metadata_source=metadata_source)
                # print(2,queryset)
            if timestamp:
                queryset = queryset.filter(timestamp__gte=timestamp)
            # print(queryset)
            logs = [{'level': entry.level,
                     'log_string': entry.log_string,
                     'timestamp': entry.timestamp,
                     'metadata_source': entry.metadata_source} for entry in queryset]

            return JsonResponse({'logs': logs})
        else:
            return JsonResponse({'error': 'Invalid data in log filter form'}, status=400)
    else:
        log_filter_form = LogFilterForm()
    return render(request, 'filter_logs.html', {'log_filter_form': log_filter_form})
