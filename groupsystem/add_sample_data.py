import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groupsystem.settings')
django.setup()

from websites.models import Website

# Add sample websites
websites_data = [
    {'name': 'Google', 'url': 'https://www.google.com', 'description': 'Search engine'},
    {'name': 'YouTube', 'url': 'https://www.youtube.com', 'description': 'Video platform'},
    {'name': 'GitHub', 'url': 'https://www.github.com', 'description': 'Code repository'},
    {'name': 'Stack Overflow', 'url': 'https://www.stackoverflow.com', 'description': 'Programming Q&A'},
]

for data in websites_data:
    website, created = Website.objects.get_or_create(
        name=data['name'],
        defaults={'url': data['url'], 'description': data['description']}
    )
    if created:
        print(f"Added: {website.name}")
    else:
        print(f"Already exists: {website.name}")

print("Sample data added successfully!")