# Generated by Django 5.0 on 2024-01-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='renteremail',
            field=models.EmailField(default='nehareddy@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='school',
            name='semail',
            field=models.EmailField(default='nehareddy@gmail.com', max_length=254),
        ),
    ]