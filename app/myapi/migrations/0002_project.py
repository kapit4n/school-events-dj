# Generated by Django 2.1.15 on 2020-04-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
