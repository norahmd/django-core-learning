# Generated by Django 3.0 on 2019-12-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='active',
            field=models.BooleanField(null=True),
        ),
    ]