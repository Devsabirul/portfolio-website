# Generated by Django 4.0.6 on 2022-08-02 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='porfile',
            new_name='profile',
        ),
    ]
