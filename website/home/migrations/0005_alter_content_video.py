# Generated by Django 4.2.3 on 2023-10-26 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='video',
            field=models.FileField(default='', upload_to='shop/videos'),
        ),
    ]