# Generated by Django 3.0.2 on 2022-07-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0015_auto_20220715_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='yoj',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
