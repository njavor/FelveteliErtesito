from django.db import models

class Tagozat(models.Model):
    class Meta:
        verbose_name = 'Tagozat'
        verbose_name_plural = 'Tagozatok'

    nev = models.CharField('név', max_length=15)
    rov = models.CharField('betű', max_length=2)

    def __str__(self) -> str:
        return self.rov + ' - ' + self.nev

class Jelentkezo(models.Model):
    class Meta:
        verbose_name = 'Jelentkező'
        verbose_name_plural = 'Jelentkezők'
    
    azonosito = models.CharField('azonosító', max_length=11)
    nev = models.CharField('név', max_length=255)
    A = models.FloatField('pontszám (A)', blank=True)
    B = models.FloatField('pontszám (B)', blank=True)
    C1 = models.FloatField('pontszám (C1)', blank=True)
    C2 = models.FloatField('pontszám (C2)', blank=True)
    D1 = models.FloatField('pontszám (D1)', blank=True)
    D2 = models.FloatField('pontszám (D2)', blank=True)
    E = models.FloatField('pontszám (E)', blank=True)
    F1 = models.FloatField('pontszám (F1)', blank=True)
    F2 = models.FloatField('pontszám (F2)', blank=True)
    tagozatok = models.ManyToManyField(Tagozat)
    felveve = models.ManyToManyField(Tagozat, related_name='felveve+')
    

    def __str__(self):
        return self.nev