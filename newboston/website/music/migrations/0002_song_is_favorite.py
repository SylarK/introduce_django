# Generated by Django 3.0.8 on 2020-07-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
