# Generated by Django 4.0.6 on 2022-08-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_alter_hero_t1_alter_hero_t2_alter_hero_t3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='heading',
            field=models.CharField(max_length=120),
        ),
    ]
