# Generated by Django 3.2.9 on 2021-11-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicas', '0003_auto_20211107_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor_profile',
            name='image',
            field=models.ImageField(default='ava_doc.jpg', null=True, upload_to=''),
        ),
    ]
