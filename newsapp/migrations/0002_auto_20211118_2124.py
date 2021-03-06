# Generated by Django 3.2.8 on 2021-11-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(help_text='This field for youtube live video link(LIVE NEWS)')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='number',
            field=models.CharField(default='', help_text='Please set the number of last news(unique,e.g. 0145)⚠use only numbers', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, unique=True),
        ),
    ]
