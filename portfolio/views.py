from django.shortcuts import render
def homepage(request):
	render(request,'home.html')