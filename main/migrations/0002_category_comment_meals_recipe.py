# Generated by Django 3.2.16 on 2022-11-20 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('longDesc', models.TextField(blank=True, max_length=1000000)),
                ('meterials', models.TextField(blank=True, max_length=1000000)),
                ('meals', models.ManyToManyField(to='main.Meals')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='main.recipe')),
            ],
        ),
    ]
