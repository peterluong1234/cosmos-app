# Generated by Django 4.0.4 on 2022-05-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_event_best_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='best_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
