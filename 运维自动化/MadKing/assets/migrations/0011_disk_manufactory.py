# Generated by Django 2.0.1 on 2019-05-09 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_auto_20170623_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='disk',
            name='manufactory',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='制造商'),
        ),
    ]
