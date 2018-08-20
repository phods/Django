from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
	template_name='courses/index.html'
	return render(request,template_name)