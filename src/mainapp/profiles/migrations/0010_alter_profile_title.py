# Generated by Django 4.2.2 on 2025-03-30 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_profile_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Title',
            field=models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], max_length=5),
        ),
    ]
