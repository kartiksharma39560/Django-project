# Generated by Django 4.2.3 on 2023-10-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_content_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='video',
        ),
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
