# Generated by Django 2.1.5 on 2019-10-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191020_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
