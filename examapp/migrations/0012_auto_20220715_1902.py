# Generated by Django 3.0.2 on 2022-07-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0011_auto_20220715_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebooksmodel',
            name='pdf',
            field=models.FileField(blank=True, default=None, upload_to='pdfs/'),
        ),
    ]
