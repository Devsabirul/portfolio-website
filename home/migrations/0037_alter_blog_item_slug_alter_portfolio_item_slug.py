# Generated by Django 4.0.6 on 2022-08-10 05:47

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_hero_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_item',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='portfolio_item',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
