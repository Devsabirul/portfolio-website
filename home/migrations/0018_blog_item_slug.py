# Generated by Django 4.0.6 on 2022-08-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_portfolio_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_item',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]