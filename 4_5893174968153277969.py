urun_listesi = {'elma': 10, 'armut': 58, 'kivi': 47, 'karpuz': 26, 'kavun': 12}
alis_fiyatı = {'elma':2,'armut':6,'kivi':7,'karpuz':8,'kavun':5}
satis_fiyati = {'elma':4,'armut':11,'kivi':12,'karpuz':10,'kavun':8}
toplam_kar = {}
while True:
    print('ürün satışı=1 ,karlılık hesapla = 2 , gün sonu =3 ,ürün ekle veya değiştir = 4, çıkış yap = 5' )
    giris = int(input('yapmak istediğin işlemin sayısını girin'))
    if giris == 1:
        print(list(urun_listesi.keys()))
        l = input('almak istediğiniz ürünü girin ')
        if l in urun_listesi:
            print('adedi girin')
            k = int(input())
        else:
            print('yanlış yazdınız ')
            continue
        if k in range(urun_listesi[l] + 1) :
            print('almak istediğiniz üründen {} kaldı '.format(urun_listesi[l]-k))
            urun_listesi[l] = urun_listesi[l]-k
            toplam_kar[l] = k * (satis_fiyati[l] - alis_fiyatı[l])
        else:
            print('almak istediğiniz üründen o kadar yok sg')
    elif giris == 4:
        print('meyve adını girin ')
        c = input()
        print('ürün adedini girin ')
        t = int(input())
        p=urun_listesi[c] = t
    elif giris == 2:
        print('{}'.format(k*(satis_fiyati[l]-alis_fiyatı[l])))
    elif giris ==3:
         p = input('yönetici girişi sağlanmalı. "Parola" giriniz ')
         if p == 'dogi':
            print(toplam_kar)
    elif giris == 5:
        break










