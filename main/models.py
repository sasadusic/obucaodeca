from django.db import models

class Marka(models.Model):
    imeMarke = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.imeMarke

class Boja(models.Model):
    boja = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.boja
    
class VelicinaObuce(models.Model):
    velicina = models.PositiveIntegerField()

    def __str__(self):
        return str(self.velicina)

class VelicinaOdece(models.Model):
    velicina = models.PositiveIntegerField()

    def __str__(self):
        return str(self.velicina)

class SlikaObuce(models.Model):
    obuca = models.ForeignKey('Obuca', related_name='slike_obuce', on_delete=models.CASCADE)
    slika = models.ImageField(upload_to='obuca_slike')

    def __str__(self):
        return f'Image for {self.obuca.naziv}'

class SlikaOdece(models.Model):
    odeca = models.ForeignKey('Odeca', related_name='slike_odece', on_delete=models.CASCADE)
    slika = models.ImageField(upload_to='odeca_slike')

    def __str__(self):
        return f'Image for {self.odeca.naziv}'

class Obuca(models.Model):
    naziv = models.CharField(max_length=100)
    cena = models.PositiveIntegerField()
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    boja = models.ForeignKey(Boja, on_delete=models.CASCADE)
    velicina = models.ForeignKey(VelicinaObuce, on_delete=models.CASCADE)
    stanje = models.CharField(max_length=50)
    opis = models.TextField()
    slike = models.ManyToManyField(SlikaObuce, related_name='obuce')

    def __str__(self):
        return self.naziv

class Odeca(models.Model):
    naziv = models.CharField(max_length=100)
    tip = models.CharField(max_length=100)
    cena = models.PositiveIntegerField()
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    boja = models.ForeignKey(Boja, on_delete=models.CASCADE)
    velicina = models.ForeignKey(VelicinaOdece, on_delete=models.CASCADE)
    stanje = models.CharField(max_length=50)
    opis = models.TextField()
    slike = models.ManyToManyField(SlikaOdece, related_name='odece')

    def __str__(self):
        return self.naziv
