# Generated by Django 2.2.13 on 2021-03-17 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='江健瑋', max_length=255, verbose_name='姓名')),
                ('name_en', models.CharField(default='willchiang', max_length=255, verbose_name='姓名（英）')),
                ('school', models.CharField(max_length=255, verbose_name='學校')),
                ('introduction', models.TextField(blank=True, verbose_name='簡介')),
            ],
            options={
                'verbose_name': '個人簡介',
                'verbose_name_plural': '個人簡介',
            },
        ),
    ]
