from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # exclude = [
        #     'slug'
        # ]
        
        fields = [
            'author',
            'title',
            'category',
            'description',
            'is_published',
        ]
        
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Input the blog title ...'
                }
            ),
            'category' : forms.Select(
                attrs = {
                    'class' : 'form-control'
                }
            ),
            'author' : forms.Select(
                attrs = {
                    'class' : 'form-control'
                }
            ),
            'description' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Insert the blog description ...'
                }
            ),
            'is_published' : forms.CheckboxInput(
                attrs = {
                    'class' : 'form-check-input ms-2'
                }
            )
        }