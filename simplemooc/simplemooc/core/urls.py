from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from simplemooc.core import views


urlpatterns = [
	#path('$',simplemooc.core.views.home),
	path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
   
]
