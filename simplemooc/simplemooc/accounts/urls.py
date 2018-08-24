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


urlpatterns = [
	

	path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('sair/', LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
	
	path('', views.dashboard, name='dashboard'),

   	path('cadastre-se/', views.register, name='register'),
   	path('nova-senha/', views.password_reset, name='password_reset'),
   	path('confirmar-nova-senha/<slug>', views.password_reset_confirm, name='password_reset_confirm'),
   	path('editar/', views.edit, name='edit'),
   	path('editar-senha/', views.edit_password, name='edit_password'),

#path('<slug>', views.password_reset_confirm, name='password_reset_confirm'),
   

]