# Generated by Django 3.0 on 2019-12-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191203_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='New Title', max_length=240),
            preserve_default=False,
        ),
    ]
