import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groupsystem.settings')
django.setup()

from websites.models import Website

# Update YouTube URL to M-E-T Hub
youtube = Website.objects.filter(name='YouTube').first()
if youtube:
    youtube.url = 'https://m-e-t-hub.onrender.com'
    youtube.name = 'M-E-T Hub'
    youtube.description = 'M-E-T Hub Platform'
    youtube.save()
    print(f"Updated YouTube to M-E-T Hub: {youtube.url}")

# Add BoardingNest
boarding_nest, created = Website.objects.get_or_create(
    name='BoardingNest',
    defaults={
        'url': 'https://boardningnest.onrender.com',
        'description': 'BoardingNest Platform'
    }
)
if created:
    print(f"Added BoardingNest: {boarding_nest.url}")
else:
    print(f"BoardingNest already exists: {boarding_nest.url}")

print("URLs updated successfully!")