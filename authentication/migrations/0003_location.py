# Generated by Django 5.1 on 2024-10-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_location_profile_job_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]