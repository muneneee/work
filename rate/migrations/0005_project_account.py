# Generated by Django 2.2 on 2020-06-07 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rate', '0004_auto_20200607_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]