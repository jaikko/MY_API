# Generated by Django 3.1.7 on 2021-04-12 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0002_auto_20210409_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributors',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='projects',
            name='type',
            field=models.CharField(blank=True, choices=[('back-end', 'back-end'), ('front-end', 'front-end'), ('IOS', 'IOS'), ('Android', 'Android')], max_length=300),
        ),
    ]
