# from django.urls import path,include
# from simplemooc.accounts import views
# from django.contrib.auth.views import login


# urlpatterns = [
	
# 	# path('entrar/', include(('django.contrib.auth.views.login',"teste"),
# 	#  	{'template_name':'accounts/login.html'}, name='login')),
# 	path('entrar/', include('django.contrib.auth.views.login',"teste")),
# 	#path('conta/', include(('simplemooc.accounts.urls',"teste"), namespace='login')),
   
# ]
from django.contrib.auth.views import LoginView,LogoutView

from django.urls import path
from . import views
from simplemooc.accounts import views


urlpatterns = [
	path('', views.dashboard, name='dashboard'),

	path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('sair/', LogoutView.as_view(template_name='simplemooc/core/home.html'), name='logout'),

   	path('cadastre-se/', views.register, name='register'),
   	path('editar/', views.edit, name='edit'),
   	path('editar-senha/', views.edit_password, name='edit_password'),

]