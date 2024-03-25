# Generated by Django 4.2.4 on 2024-03-21 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Life Style', 'Life Style'), ('Technology', 'Technology'), ('Education', 'Education'), ('Entertaiment', 'Entertaiment')], default='Life Style', max_length=255)),
                ('is_published', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('published', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
            ],
            options={
                'permissions': (('publish_blog', 'Can publish blog'),),
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
    ]