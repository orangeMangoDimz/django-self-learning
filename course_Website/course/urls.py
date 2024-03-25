from django.urls import path
from .views import update, DeleteView, CourseFormView

app_name = 'course'

urlpatterns = [
    path('create/', CourseFormView.as_view(template_name= 'course/create.html', mode='create'), name='course_create'),
    path('update/<slug>/', CourseFormView.as_view(template_name='course/update.html', mode='update'), name='course_edit'),
    path('delete/<courseId>', DeleteView.as_view(), name='course_delete')
]
