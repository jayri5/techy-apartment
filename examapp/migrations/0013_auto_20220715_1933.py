# Generated by Django 3.0.2 on 2022-07-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0012_auto_20220715_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebooksmodel',
            name='pdf',
            field=models.FileField(blank=True, upload_to='pdfs/'),
        ),
    ]