# Generated by Django 3.0 on 2019-12-03 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191203_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
