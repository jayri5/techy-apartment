# Generated by Django 3.0.2 on 2022-06-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0004_students_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
    ]
