# Generated by Django 4.2.2 on 2025-03-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_alter_profile_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Title',
            field=models.CharField(blank=True, choices=[('Ms', 'Ms'), ('Mrs', 'Mrs'), ('Mr', 'Mr')], max_length=5),
        ),
    ]
