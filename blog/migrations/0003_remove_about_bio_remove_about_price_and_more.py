# Generated by Django 5.1.1 on 2024-12-04 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='about',
            name='price',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='price',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='price',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='price',
        ),
        migrations.RemoveField(
            model_name='team',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='team',
            name='price',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='price',
        ),
    ]
