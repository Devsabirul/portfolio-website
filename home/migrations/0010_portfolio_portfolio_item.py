# Generated by Django 4.0.6 on 2022-08-03 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_p_skill_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('Picture', models.ImageField(upload_to='images/')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
