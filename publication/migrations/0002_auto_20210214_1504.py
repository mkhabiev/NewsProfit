# Generated by Django 3.1.5 on 2021-02-14 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]