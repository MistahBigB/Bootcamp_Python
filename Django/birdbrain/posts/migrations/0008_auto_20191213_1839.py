# Generated by Django 3.0 on 2019-12-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20191213_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brain',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
