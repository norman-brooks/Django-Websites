# Generated by Django 4.2.2 on 2025-03-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_profile_delete_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Title',
            field=models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')], max_length=5),
        ),
    ]
