from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return '{}. {}'.format(self.id, self.name)

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(
        max_length = 255,
    )
    category = models.CharField(
        max_length = 255,
        choices = (
            ('Life Style', 'Life Style'),
            ('Technology', 'Technology'),
            ('Education', 'Education'),
            ('Entertaiment', 'Entertaiment')
        ),
        default = 'Life Style',
    )
    is_published = models.BooleanField(default=False)
    description = models.TextField()
    published = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, editable = False)
    
    class Meta:
        default_permissions = ('add', 'change', 'delete') # By default it will contains 4: add, cahnge, delete, view
        permissions = ( 
            ('publish_blog', 'Can publish blog'),
        ) # custom permissions
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.is_published == True:
            self.published = timezone.now()
        super(Blog, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return '{}. {}'.format(self.id, self.title)
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
