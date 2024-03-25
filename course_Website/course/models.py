from django.db import models
from django.utils.text import slugify
from .validators import validate_title

# Create your models here.

class Course(models.Model):
    title = models.CharField(
        max_length = 255,
        validators = [
            validate_title
        ]
    )
    category = models.CharField(
        max_length = 255,
        choices = (
            ('Math', 'math'),
            ('Database', 'database'),
            ('Artificial Intelegence', 'artificial_intelegence'),
            ('Internet of Things', 'internet_of_things')
        ),
        default = 'Math',
    )
    description = models.TextField()
    timestamps = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(max_length=255, unique=True, editable = False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)
    
    def __str__(self):
        return "{}".format(self.title)
