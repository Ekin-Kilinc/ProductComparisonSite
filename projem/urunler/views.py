from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Urunler
from .models import Inceleme
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

def urunlerSayfasi(request):
 sablon = loader.get_template('liste.html')
 return HttpResponse(sablon.render())

def urunIncele(request):
 sablon = loader.get_template('inceleme.html')
 return HttpResponse(sablon.render())

def urunKarsilastir(request):
 sablon = loader.get_template('karsilastirma.html')
 return HttpResponse(sablon.render())
def urunDetay(request, urunid):
 bilgi = {'urun' : Urunler.objects.get(id = urunid)}
 sablon = loader.get_template('detay.html')
 return HttpResponse(sablon.render(bilgi, request))

def urunDuzenle(request, urunid):
 bilgi = {'urun' : Urunler.objects.get(id = urunid), 'guncellendimi': "False"}
 hatalar = []
 if request.method == 'POST':
     urun = Urunler.objects.get(id=urunid)
     urun.ad = request.POST['ad']
     urun.fiyat = request.POST['fiyat']

     urunResmi = request.FILES.get('urunResmi', False)
     if urunResmi != False:
         if urunResmi.name.split(".")[-1] in ['jpg', 'png']:
             fs = FileSystemStorage()
             yukle = fs.save('images/' + urunResmi.name, urunResmi)
             urunResmi_url = fs.url(yukle)
             urun.urunResmi=urunResmi_url
         else:
             hatalar.append("Sadece jpg veya png uzantılı resim yüklenebilir!")
     else:
         hatalar.append("Ürün resmi boş olamaz!")

     urun.urunaciklama = request.POST['urunaciklama']
     urun.stokdurumu = request.POST.get('stokdurumu', False)
     if urun.stokdurumu == "on":
         urun.stokdurumu = True
     urun.save()
     bilgi['urun'] = urun
     bilgi['guncellendimi'] = "True"
 sablon = loader.get_template('duzenle.html')
 return HttpResponse(sablon.render(bilgi, request))


@csrf_exempt
def yeniurun(request):
 hatalar = []
 bilgi = {'yeniKayit' : "False", 'hatalistesi' : hatalar}
 if request.method == 'POST':

   ad = request.POST['ad']
   if len(ad) < 1:
       hatalar.append("Ürün adı 1 karakterden küçük olamaz!")

   fiyat = request.POST['fiyat']
   if len(fiyat) == 0 or int(fiyat, 10) < 0:
       hatalar.append("Fiyat boş veya negatif olamaz!")

   urunResmi = request.FILES.get('urunResmi', False)
   if urunResmi != False:
       if urunResmi.name.split(".")[-1] in ['jpg', 'png']:
            fs = FileSystemStorage()
            yukle = fs.save('images/' + urunResmi.name, urunResmi)
            urunResmi_url = fs.url(yukle)
       else:
            hatalar.append("Sadece jpg veya png uzantılı resim yüklenebilir!")
   else:
       hatalar.append("Ürün resmi boş olamaz!")

   urunno = request.POST['urunno']
   if len(urunno) == 0 or int(urunno, 10) < 0:
       hatalar.append("Ürün no boş veya negatif olamaz!")
   stokdurumu = request.POST.get('stokdurumu', False)
   if stokdurumu =="on":
    stokdurumu = True
   if len(hatalar) == 0:
       yeniUrun = Urunler(ad=ad, fiyat=fiyat, urunResmi=urunResmi_url, urunno=urunno, stokdurumu=stokdurumu)
       yeniUrun.save()
       bilgi['yeniKayit'] = "True"
   else :
       bilgi['hatalistesi'] = hatalar
 sablon = loader.get_template('yeni.html')
 return HttpResponse(sablon.render(bilgi,request))

def urunSepet(request):
 if request.method == 'POST':
     silinecek = request.POST['sil']
     Urunler.objects.get(id=silinecek).delete()
 urunlistesi = Urunler.objects.all()
 sablon = loader.get_template('sepet.html')
 veriler = {
  'urunlistesi':urunlistesi
 }
 return HttpResponse(sablon.render(veriler, request))



def urunDetay2(request, urunid):
 bilgi = {'urun' : Inceleme.objects.get(id = urunid)}
 sablon = loader.get_template('detay2.html')
 return HttpResponse(sablon.render(bilgi, request))
def urunDuzenle2(request, urunid):
 bilgi = {'urun' : Inceleme.objects.get(id = urunid), 'guncellendimi': "False"}
 hatalar = []
 if request.method == 'POST':
     urun = Inceleme.objects.get(id=urunid)
     urun.inceleme = request.POST['inceleme']
     urun.save()
     bilgi['urun'] = urun
     bilgi['guncellendimi'] = "True"
 sablon = loader.get_template('duzenle2.html')
 return HttpResponse(sablon.render(bilgi, request))

def yeniurun2(request):
    hatalar = []
    bilgi = {'yeniKayit': "False", 'hatalistesi': hatalar}
    available_products = Urunler.objects.all()

    if request.method == 'POST':
        urun = request.POST['urun']
        if len(urun) < 1:
            hatalar.append("Ürün adı 1 karakterden küçük olamaz!")

        inceleme = request.POST['inceleme']
        if len(inceleme) < 1:
            hatalar.append("İnceleme boş veya negatif olamaz!")

        if len(hatalar) == 0:
            # Modify this part to get the selected product
            selected_product_id = request.POST['urun']
            selected_product = Urunler.objects.get(id=selected_product_id)

            yeniUrun2 = Inceleme(urun=selected_product, inceleme=inceleme)
            yeniUrun2.save()
            bilgi['yeniKayit'] = "True"
        else:
            bilgi['hatalistesi'] = hatalar

    bilgi['available_products'] = available_products
    return render(request, 'yeni2.html', bilgi)

def sepetInceleme(request):
    if request.method == 'POST':
        silinecek = request.POST['sil']
        Inceleme.objects.get(id=silinecek).delete()
    urunlistesi2 = Inceleme.objects.all()
    sablon = loader.get_template('sepet_inceleme.html')
    veriler = {
        'urunlistesi2': urunlistesi2
    }
    return HttpResponse(sablon.render(veriler, request))