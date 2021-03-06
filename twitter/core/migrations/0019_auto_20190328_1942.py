# Generated by Django 2.1.7 on 2019-03-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_user_theme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='theme',
            new_name='dark_theme',
        ),
        migrations.AddField(
            model_name='user',
            name='is_dark',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='light_theme',
            field=models.CharField(default='https://unpkg.com/bulmaswatch/cerulean/bulmaswatch.min.css', max_length=200),
        ),
    ]
