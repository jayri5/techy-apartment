# Generated by Django 3.0.2 on 2022-07-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0013_auto_20220715_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebooksmodel',
            name='pdf',
            field=models.FileField(blank=True, default=' ', upload_to='pdfs/'),
        ),
    ]
