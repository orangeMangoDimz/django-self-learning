from typing import Any
from django.shortcuts import render, get_object_or_404
from course.models import Course
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

# * FUNCTION BASE
# def dashboard(request):
#     categories = Course.objects.values('category').distinct()
#     courses = Course.objects.values()
#     context = {
#         "courses" : courses, 
#         "categories" : categories
#     }
#     return render(request, 'index.html', context)

# def category_filter(request, category):
#      categories = Course.objects.values('category').distinct()
#      courses = Course.objects.filter(category=category)
#      context = {
#         "courses" : courses, 
#         "categories" : categories
#     }
#      return render(request, 'index.html' ,context)


class CourseFilter:
    def course_filter(self, content):
        if len(content) == 0:
            return Course.objects.all()
        elif 'category' in content:
            # return get_object_or_404(Course, category=content.get('category'))
            return Course.objects.filter(category__iexact=content.get('category'))
        else:
            print('unknown')
            return Course.objects.none()
        

# * TEMPLATE VIEW 
class DashboardView(CourseFilter, TemplateView):
    template_name = 'index.html'
    def get_context_data(self):
            categories = Course.objects.values('category').distinct()
            # courses = Course.objects.values()
            courses = self.course_filter(self.request.GET)
            context = {
                "courses" : courses, 
                "categories" : categories
            }
            return context


 
class CategoryView(RedirectView):
    pattern_name = 'main:home'
    
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
         return super().get_redirect_url(*args, **kwargs)
 
class About(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Us"
        context["description"] = "This is a demo website to test a django project for creating a Course App Project"
        return context