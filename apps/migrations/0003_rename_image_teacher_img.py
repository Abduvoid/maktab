# Generated by Django 5.1.2 on 2025-03-01 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_gallery_name_gallery_title_alter_gallery_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='image',
            new_name='img',
        ),
    ]
