from django.contrib import admin
from django.urls import path,include
from simplemooc.courses import views


urlpatterns = [
	#path('$',simplemooc.core.views.home),
	path('', views.index1, name='index1'),
	#path('<int:pk>', views.details, name='details'),
    path('<slug>', views.details, name='details'),
   
]
