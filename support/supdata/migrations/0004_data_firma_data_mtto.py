# Generated by Django 5.2 on 2025-04-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supdata', '0003_data_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='firma',
            field=models.ImageField(blank=True, null=True, upload_to='firmas/'),
        ),
        migrations.AddField(
            model_name='data',
            name='mtto',
            field=models.ManyToManyField(to='supdata.revision'),
        ),
    ]
