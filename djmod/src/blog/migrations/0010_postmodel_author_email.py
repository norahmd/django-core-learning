# Generated by Django 3.0 on 2019-12-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191203_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='author_email',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]
