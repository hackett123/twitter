# Generated by Django 2.1.7 on 2019-03-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190323_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='num_usages',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='hashtags',
            field=models.ManyToManyField(to='core.Hashtag'),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]