from django.urls import path, include
from .views import loginView, register, logoutView

# from .views import 

app_name = 'auth'

urlpatterns = [
    # path('login/', AuthView.as_view(template_name = 'auth/login.html'), name='login'),
    # path('register/', AuthView.as_view(template_name = 'auth/register.html'), name='register')
    path('login/', loginView, name='login'),
    path('register/', register, name='register'),
    path('logout/', logoutView, name='logout')
]
