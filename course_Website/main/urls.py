from django.urls import path, include
from .views import DashboardView, About, CategoryView

app_name = 'main'

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('course/', include('course.urls', namespace='course')),
]
