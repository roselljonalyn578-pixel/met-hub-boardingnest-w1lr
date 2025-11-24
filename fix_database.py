import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groupsystem.settings')
django.setup()

from websites.models import Website

# Clear all existing websites
Website.objects.all().delete()

# Add only the two websites you want
Website.objects.create(
    name='M-E-T Hub',
    url='https://m-e-t-hub.onrender.com',
    description='M-E-T Hub Platform'
)

Website.objects.create(
    name='BoardingNest',
    url='https://boardingnest-w1lr.onrender.com/',
    description='BoardingNest Platform'
)

print("Database updated with M-E-T Hub and BoardingNest only!")