# Generated by Django 3.2.9 on 2021-11-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicas', '0013_alter_mota_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='danh_sach_sp',
            name='INFO',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
