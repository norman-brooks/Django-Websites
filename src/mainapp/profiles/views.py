from django.shortcuts import render
from .models import Profile

# Home page view
def admin_console(request):
    profiles = Profile.objects.all()  # Fetch all profiles from the database
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles})


