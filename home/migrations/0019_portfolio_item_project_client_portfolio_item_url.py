# Generated by Django 4.0.6 on 2022-08-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_blog_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_item',
            name='project_client',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolio_item',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
