from django.db import models

class Urunler(models.Model):
    urunno = models.IntegerField()
    ad = models.CharField(max_length=600)
    fiyat = models.CharField(max_length=700)
    stokdurumu = models.CharField(max_length=60)
    acıklama = models.CharField(max_length=10000)
    urunResmi = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.ad} {self.urunno}"

class Inceleme(models.Model):
    urun = models.ForeignKey(Urunler, on_delete=models.CASCADE)
    inceleme = models.CharField(max_length=10000)

    def __str__(self):
        return f"{self.urun} {self.inceleme}"