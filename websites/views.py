from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Website
from .forms import WebsiteForm

def website_list(request):
    websites = Website.objects.all()
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