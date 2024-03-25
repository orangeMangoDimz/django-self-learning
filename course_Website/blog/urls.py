from django.urls import path, include
from .views import BlogView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from .forms import BlogForm
# from .views import 

app_name = 'blog'

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<pk>', BlogUpdateView.as_view(), name='update'),
    path('delete/<pk>', BlogDeleteView.as_view(), name='delete'),
    path('<page>', BlogView.as_view(), name='index'),
    path('<category>/<page>', BlogView.as_view(), name='category'),
    path('detail/<slug>/', BlogDetailView.as_view(), name='detail'),
]
