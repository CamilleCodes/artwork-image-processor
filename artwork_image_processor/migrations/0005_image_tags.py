# Generated by Django 2.1.2 on 2018-11-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork_image_processor', '0004_auto_20181016_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
