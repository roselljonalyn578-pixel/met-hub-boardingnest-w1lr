from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from .models import Website
from .forms import WebsiteForm

def website_list(request):
    try:
        # Check if table exists
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='websites_website';")
            if not cursor.fetchone():
                # Create table if it doesn't exist
                from django.core.management import execute_from_command_line
                execute_from_command_line(['manage.py', 'migrate'])
        
        websites = Website.objects.all()
        
        # Add sample data if empty
        if not websites.exists():
            Website.objects.create(name='M-E-T Hub', url='https://m-e-t-hub.onrender.com', description='M-E-T Hub Platform')
            Website.objects.create(name='BoardingNest', url='https://boardingnest-w1lr.onrender.com/', description='BoardingNest Platform')
            websites = Website.objects.all()
            
    except Exception as e:
        websites = []
    
    return render(request, 'websites/list.html', {'websites': websites})

def add_website(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Website added successfully!')
            return redirect('website_list')
    else:
        form = WebsiteForm()
    return render(request, 'websites/add.html', {'form': form})