# Generated by Django 4.0.6 on 2022-08-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_portfolio_item_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio_item',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
