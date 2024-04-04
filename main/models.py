from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Marka(models.Model):
    imeMarke = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.imeMarke

class Boja(models.Model):
    boja = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.boja
    
class VelicinaObuce(models.Model):
    velicina = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.velicina)

class VelicinaOdece(models.Model):
    velicina = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.velicina)

class SlikaObuce(models.Model):
    obuca = models.ForeignKey('Obuca', related_name='slike_obuce', on_delete=models.CASCADE)
    slika = models.ImageField(null=True, blank=True, upload_to='obuca_slike')

    def __str__(self):
        return str(self.slika)

class SlikaOdece(models.Model):
    odeca = models.ForeignKey('Odeca', related_name='slike_odece', on_delete=models.CASCADE)
    slika = models.ImageField(null=True, blank=True, upload_to='odeca_slike')

    def __str__(self):
        return f'Image for {self.odeca.naziv}'
    
@receiver(post_delete, sender=SlikaObuce)
def delete_slikaobuce_file(sender, instance, **kwargs):
    # Delete file from filesystem when corresponding `SlikaObuce` object is deleted.
    if instance.slika:
        if os.path.isfile(instance.slika.path):
            os.remove(instance.slika.path)

class Obuca(models.Model):
    naziv = models.CharField(max_length=100)
    sifra = models.PositiveIntegerField(null=True, blank=True, unique=True)
    cena = models.PositiveIntegerField()
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    boja = models.ManyToManyField(Boja)
    velicina = models.ManyToManyField(VelicinaObuce)
    stanje = models.CharField(max_length=50, null=True, blank=True)
    opis = models.TextField(null=True, blank=True)
    glavnaSlika = models.ImageField(upload_to='obuca_slike', null=True, blank=True)
    slike = models.ManyToManyField(SlikaObuce, related_name='obuce', null=True, blank=True)

    def __str__(self):
        return self.naziv

class Odeca(models.Model):
    naziv = models.CharField(max_length=100)
    sifra = models.PositiveIntegerField(null=True, blank=True, unique=True)
    tip = models.CharField(max_length=100)
    cena = models.PositiveIntegerField()
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    boja = models.ManyToManyField(Boja)
    velicina = models.ManyToManyField(VelicinaOdece)
    stanje = models.CharField(max_length=50)
    opis = models.TextField()
    slike = models.ManyToManyField(SlikaOdece, related_name='odece')

    def __str__(self):
        return self.naziv