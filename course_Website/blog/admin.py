from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Blog, Author
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    ## aadd this for permission check
    def get_readonly_fields(self, request: HttpRequest, obj: Any | None = ...) -> list[str] | tuple[Any, ...]:
        if request.user.has_perm('blog.publish_blog'):
            if obj is not None:
                if obj.is_published:
                    print("obj : ", obj.is_published)
                    return [data.name for data in self.model._meta.fields]
            readonly_fields = [
                'created_at',
                'updated_at',
                'published',
                'slug',
            ]
        else:
            if request.user.has_perm('blog.add_blog'):
                readonly_fields = [
                    'created_at',
                    'updated_at',
                    'is_published',
                    'published',
                    'slug',
                ]
        return readonly_fields

    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)