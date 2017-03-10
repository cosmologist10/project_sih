from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home_page(request):
	return render(request, 'home_and_login/home_page.html')