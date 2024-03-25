from django import forms
from .models import Course

# class CourseForm(forms.Form):
#     title = forms.CharField(
#         label='Title',
#         max_length=50,
#         widget=forms.TextInput(
#             attrs={
#                 'class' : 'form-control',
#                 'placeholder' : 'Input your title here ...'
#             }
#         )
#     )
#     description = forms.CharField(
#         label='Description', 
#         widget=forms.Textarea(
#             attrs={
#                 'class' :  'form-control',
#                 'placeholder' : 'Input your description here ...'
#             }
#         )
#     )
    
#     def clean_title(self):
#         data = self.cleaned_data["title"]
#         if len(data):
#             raise forms.ValidationError('Title cannot be empty!')
#         return data

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = [
            "timestamps",
            "slug"
        ] # exclude the fields you don't want in the form
        
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Input the course title ...'
                }
            ),
            'category' : forms.Select(
                attrs = {
                    'class' : 'form-control'
                }
            ),
            'description' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Insert the course description ...'
                }
            )
        }