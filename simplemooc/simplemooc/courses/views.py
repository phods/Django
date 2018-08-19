from django.shortcuts import render

# Create your views here.
def courses(request):
	template_name='courses/courses.html'
	return render(request,template_name)