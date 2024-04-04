# Generated by Django 5.0.3 on 2024-04-03 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_obuca_sifra_odeca_sifra_alter_velicinaobuce_velicina_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obuca',
            name='boja',
        ),
        migrations.RemoveField(
            model_name='obuca',
            name='velicina',
        ),
        migrations.RemoveField(
            model_name='odeca',
            name='boja',
        ),
        migrations.RemoveField(
            model_name='odeca',
            name='velicina',
        ),
        migrations.AddField(
            model_name='obuca',
            name='boja',
            field=models.ManyToManyField(to='main.boja'),
        ),
        migrations.AddField(
            model_name='obuca',
            name='velicina',
            field=models.ManyToManyField(to='main.velicinaobuce'),
        ),
        migrations.AddField(
            model_name='odeca',
            name='boja',
            field=models.ManyToManyField(to='main.boja'),
        ),
        migrations.AddField(
            model_name='odeca',
            name='velicina',
            field=models.ManyToManyField(to='main.velicinaodece'),
        ),
    ]