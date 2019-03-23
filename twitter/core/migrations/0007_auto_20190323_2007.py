# Generated by Django 2.1.7 on 2019-03-23 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190323_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
