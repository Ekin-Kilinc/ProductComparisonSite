from django.contrib import admin
from .models import Urunler, Inceleme
class UrunlerAdmin(admin.ModelAdmin):
    list_display = ("urunno", "ad", "fiyat", "stokdurumu", "acıklama")

class IncelemeAdmin(admin.ModelAdmin):
    list_display = ("urun", "inceleme")

admin.site.register(Urunler, UrunlerAdmin)
admin.site.register(Inceleme, IncelemeAdmin)