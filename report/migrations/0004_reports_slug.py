# Generated by Django 4.2.2 on 2024-03-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_alter_reports_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
