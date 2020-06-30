from django.shortcuts import render, get_object_or_404
from . models import blog


def allblogs(request):

	blig= blog.objects
	return render(request,'blog/allblogs.html',{'blig':blig})

def detail(request,blog_id):
	
	dtlog=get_object_or_404(blog, pk=blog_id)
	return render(request,'blog/detail.html',{'dtlog':dtlog})

# Create your views here.
