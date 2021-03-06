# Generated by Django 3.0.8 on 2020-08-01 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0003_auto_20200801_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='owner',
            new_name='user',
        ),
        migrations.AddField(
            model_name='posts',
            name='countLike',
            field=models.IntegerField(default=0, verbose_name='Likes'),
        ),
        migrations.AddField(
            model_name='posts',
            name='countUnlike',
            field=models.IntegerField(default=0, verbose_name='Unlike'),
        ),
        migrations.AddField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data de Criação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='text',
            field=models.TextField(default=1, verbose_name='Texto: '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='Título: '),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
