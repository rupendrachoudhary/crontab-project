from django.shortcuts import render



def home(request):
	return render(request, "cronapp/home.html")

def blog(request):
	return render(request, 'cronapp/blog.html')

def contact(request):
	return render(request, 'cronapp/contact.html')