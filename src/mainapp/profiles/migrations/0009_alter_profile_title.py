# Generated by Django 4.2.2 on 2025-03-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_profile_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Title',
            field=models.CharField(blank=True, choices=[('Ms', 'Ms'), ('Mrs', 'Mrs'), ('Mr', 'Mr')], max_length=5),
        ),
    ]
