# from django.urls import path,include
# from simplemooc.accounts import views
# from django.contrib.auth.views import login


# urlpatterns = [
	
# 	# path('entrar/', include(('django.contrib.auth.views.login',"teste"),
# 	#  	{'template_name':'accounts/login.html'}, name='login')),
# 	path('entrar/', include('django.contrib.auth.views.login',"teste")),
# 	#path('conta/', include(('simplemooc.accounts.urls',"teste"), namespace='login')),
   
# ]
from django.contrib.auth.views import LoginView

from django.urls import path
from . import views
from simplemooc.accounts import views

urlpatterns = [
	path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
   	path('cadastre-se/', views.register, name='register'),

]