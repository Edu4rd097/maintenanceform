# Generated by Django 5.2 on 2025-04-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supdata', '0002_rename_opcionesrevisiom_revision_opcionesrevision_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='comentarios',
            field=models.TextField(default='Agregar comentarios acerca del equipo, tiene un valor maximo de 300 caracteres, sea breve', max_length=300),
            preserve_default=False,
        ),
    ]
