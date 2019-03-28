# Generated by Django 2.1.7 on 2019-03-28 01:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190327_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blocked_users',
            field=models.ManyToManyField(related_name='_user_blocked_users_+', to=settings.AUTH_USER_MODEL),
        ),
    ]