import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groupsystem.settings')
django.setup()

from websites.models import Website

# Remove unwanted websites
websites_to_remove = ['Google', 'GitHub', 'Stack Overflow', 'Reddit', 'Twitter']

for name in websites_to_remove:
    deleted_count = Website.objects.filter(name=name).delete()[0]
    if deleted_count > 0:
        print(f"Removed: {name}")
    else:
        print(f"Not found: {name}")

print("Cleanup completed! Only M-E-T Hub and BoardingNest remain.")