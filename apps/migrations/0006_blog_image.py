# Generated by Django 5.1.2 on 2025-03-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=1, upload_to='blog/'),
            preserve_default=False,
        ),
    ]
