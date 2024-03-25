from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course
from .forms import CourseForm
from django.views import View
from django.views.generic.base import RedirectView
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

# * FUNCTION BASE CREATE
# def create(request):
#     form = CourseForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     return render(request, 'course/create.html', { 'course_form' : form })


# * FUNCTION BASE UPDATE
def update(request, slug=''):
    course = get_object_or_404(Course, slug=slug)
    form = CourseForm(request.POST or None, initial = {
        'title' : course.title,
        'category' : course.category,
        'description' : course.description
    }, instance = course)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main:home')
    
    return render(request, 'course/update.html', { 
            'course' : course,
            'form' : form
        }
    )

# * FUNCTION BASE DELETE
# def delete(request, courseId):
#     if request.method == 'POST':
#         Course.objects.get(id = courseId).delete()
#         return redirect('main:home')


class CourseFormView(View):
    template_name = ''
    mode = ''
    form = CourseForm()    
    
    def get(self, *args, **kwargs):
        # Check group
        test_group = Group.objects.get(name='creator')
        user_group = self.request.user.groups.all()
        
        if test_group not in user_group:
            return redirect('main:home')    
        
        if self.mode == 'update': 
            course = get_object_or_404(Course, slug=kwargs['slug'])
            data = course.__dict__
            form = CourseForm(initial=data, instance=course)
            return render(self.request, self.template_name, { 'course' : course, 'course_form' : form })
        
        return render(self.request, self.template_name, { 'course_form' : self.form })
    
    def post(self, *args, **kwargs):
        if kwargs.__contains__('slug'): # ? For Update
            course = get_object_or_404(Course, slug=kwargs['slug'])
            self.form = CourseForm(self.request.POST, instance=course)
        else: # ? For Create
            self.form = CourseForm(self.request.POST)
            
        if self.form.is_valid:
            self.form.save()
        return redirect('main:home')
    
# class CreateView(View):
#     template_name = ''
    
#     # override method GET
#     def get(self, request):
#         form = CourseForm(request.POST or None)
#         return render(request, self.template_name, { 'course_form' : form })
        
#     # override method POST
#     def post(self, request):
#         form = CourseForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             return redirect('main:home')

# @user_passes_test(lambda user: Group.objects.get(name='creator') in user.groups.all(), login_url='main:home')
class DeleteView(RedirectView):
    pattern_name = 'main:home'
    
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        Course.objects.get(id = kwargs['courseId']).delete()
        return super().get_redirect_url(*args, **kwargs)
    