from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)
from django.urls import reverse_lazy
from .models import (Category, Article)

def index(request):
    # Get the current time converted to Australia/Melbourne
    melbourne_time = timezone.localtime(timezone.now())
    
    # Format it cleanly (e.g., "Thursday, 01 October 2026 - 11:20 AM")
    formatted_date = melbourne_time.strftime("%A, %d %B %Y - %I:%M %p")

    # Dynamically look up the URL pattern named 'category_list'
    category_url = reverse_lazy('categories')
    
    return HttpResponse (f"<p>Hello World! The current Melbourne time is: {formatted_date}</p><a href='{category_url}'>View News Categories</a>")

class CategoryListView(ListView):
    model = Category
    template_name = "categories.html"
    context_object_name = "categories"