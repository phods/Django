from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Course

# Create your views here.
def index1(request):
	courses=Course.objects.all()	
	context={
		'courses':courses

	}
	template_name='courses/index.html'

	return render(request,template_name,context)

# def details(request,pk):
# 	courses = get_object_or_404(Course,pk=pk)
# 	context={
# 		'course':courses
# 	}
# 	template_name='courses/details.html'
	
# 	return render(request,template_name,context)

def details(request,slug):
	courses = get_object_or_404(Course,slug=slug)
	context={
		'course':courses
	}
	template_name='courses/details.html'
	
	return render(request,template_name,context)