# Generated by Django 2.2 on 2020-06-07 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0006_choice_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rate.Project'),
            preserve_default=False,
        ),
    ]
