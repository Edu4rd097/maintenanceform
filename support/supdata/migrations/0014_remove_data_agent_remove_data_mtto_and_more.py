# Generated by Django 5.2 on 2025-04-23 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supdata', '0013_alter_agentes_borrartemporales_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='data',
            name='mtto',
        ),
        migrations.AddField(
            model_name='data',
            name='aplicacionpasta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='borrartemporales',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='encriptacionhdd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='epc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='limpexterna',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='limpiezadisipador',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='limpinterna',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='limppasta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='limpram',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='limpteclado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='limpventilador',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='sophos',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='tenable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='updates',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='agentes',
        ),
        migrations.DeleteModel(
            name='revision',
        ),
    ]
