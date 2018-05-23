from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'login/home_page.html')

def profile(request):
	return render(request, 'login/profile_home.html')