# Generated by Django 4.0.6 on 2022-08-04 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_blog_item_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('fb', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('ln', models.CharField(max_length=100)),
            ],
        ),
    ]
