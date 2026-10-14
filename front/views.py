from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone  # 1. Import Django's timezone tool

def index(request):
    # Get the current time converted to Australia/Melbourne
    melbourne_time = timezone.localtime(timezone.now())
    
    # Format it cleanly (e.g., "Thursday, 01 October 2026 - 11:20 AM")
    formatted_date = melbourne_time.strftime("%A, %d %B %Y - %I:%M %p")
    
    return HttpResponse(f"Hello World! The current Melbourne time is: {formatted_date}")
