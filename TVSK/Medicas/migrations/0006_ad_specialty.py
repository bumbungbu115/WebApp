# Generated by Django 3.2.9 on 2021-11-10 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicas', '0005_alter_advisor_profile_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=50)),
            ],
        ),
    ]
