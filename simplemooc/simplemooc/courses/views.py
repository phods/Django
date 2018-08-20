from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Course
from .forms import ContactCourse

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
	if request.method=='POST':
		form=ContactCourse(request.POST)
		 
	else:
		form= ContactCourse()

	context={
		'course':courses,
		'form':form
	}
	template_name='courses/details.html'
	
	return render(request,template_name,context)