# Generated by Django 5.0.3 on 2024-04-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_obuca_boja_remove_obuca_velicina_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odeca',
            name='velicina',
            field=models.ManyToManyField(to='main.velicinaobuce'),
        ),
    ]
