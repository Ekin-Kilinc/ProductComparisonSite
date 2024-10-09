from django.urls import path
from . import views


urlpatterns = [
 path('liste', views.urunlerSayfasi),
 path('incele/', views.urunIncele),
 path('karsilastir/', views.urunKarsilastir),
 path('detay/<int:urunid>', views.urunDetay),
 path('duzenle/<int:urunid>', views.urunDuzenle),
 path('yeniurun', views.yeniurun),
 path('sepet', views.urunSepet),
 path('detay2/<int:urunid>', views.urunDetay2),
 path('duzenle2/<int:urunid>', views.urunDuzenle2),
 path('yeniurun2', views.yeniurun2),
 path('uruninceleme', views.sepetInceleme),
]
