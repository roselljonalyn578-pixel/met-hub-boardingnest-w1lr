import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groupsystem.settings')
django.setup()

from websites.models import Website

# Update BoardingNest URL
boardingnest = Website.objects.filter(name='BoardingNest').first()
if boardingnest:
    boardingnest.url = 'https://boardingnest-w1lr.onrender.com/'
    boardingnest.save()
    print(f"Updated BoardingNest URL to: {boardingnest.url}")
else:
    print("BoardingNest not found")

print("URL update completed!")