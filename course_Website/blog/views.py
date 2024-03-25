from typing import Any
from django.shortcuts import render
from django.views.generic import (
        ListView, 
        DetailView,
        FormView, 
        CreateView,
        UpdateView, 
        DeleteView
    )
from .models import Blog
from django.core.paginator import InvalidPage
from .forms import BlogForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required

# Create your views here.

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:index', kwargs={
        'page' : 1
    })
    template_name = 'blog/blog_confirm_delete.html'

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/update.html'
    extra_context = {
        'page_title' : 'Update Blog'
    }
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

class BlogCreateView(CreateView):
    form_class = BlogForm
    template_name = "blog/create.html"
    
    extra_context = {
        'page_title' : 'Create a New Blog'
    }
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

class BlogFormView(FormView):
    form_class = BlogForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:index', kwargs = {
        'page' : 1
    })
    extra_context = {
        'page_title' : 'Create a New Blog'
    }
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class BlogView(ListView):
    model = Blog
    ordering = ['title']
    paginate_by = 3
    categories = Blog.objects.values('category').distinct()
    extra_content = {
        'page_title' : 'My Blog',
        'categories' : categories
    }
    
    def get_queryset(self):
        if 'category' in self.kwargs:
            self.queryset = self.model.objects.filter(category = self.kwargs['category'])
            self.kwargs.update({
                'category' : self.kwargs['category']
            })
        return super().get_queryset()
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        self.kwargs.update(self.extra_content)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        slug = self.kwargs.get('slug')
        blog = self.model.objects.get(slug=slug)
        other_blos = self.model.objects.exclude(slug=slug)
        extra_content = {
            'page_title' : blog.title,
            'other_blogs' : other_blos
        }
        self.kwargs.update(extra_content)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)