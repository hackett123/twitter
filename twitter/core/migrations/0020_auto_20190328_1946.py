# Generated by Django 2.1.7 on 2019-03-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20190328_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dark_theme',
        ),
        migrations.RemoveField(
            model_name='user',
            name='light_theme',
        ),
        migrations.AddField(
            model_name='user',
            name='theme',
            field=models.CharField(default='https://unpkg.com/bulmaswatch/cerulean/bulmaswatch.min.css', max_length=256),
        ),
    ]
