# Nitel Görüşme Kodlama Defteri

Bu proje, sosyologların görüşme alıntılarını takma kodlarla kaydetmesine, bir alıntıya birden fazla tema vermesine ve tema sayılarını özetlemesine yardımcı olan basit bir komut satırı uygulamasıdır. Alıntılar gerçek kişileri tanıtacak ayrıntılardan kullanıcı tarafından arındırılmalıdır; uygulama otomatik anonimleştirme yapmaz.

## Nasıl çalıştırılır

1. ZIP dosyasını çıkarın ve `sosyoloji_nitel_kodlama` klasörünü açın.
2. Terminal'i açıp bu klasöre geçin.
3. `python3 uygulama.py` komutunu çalıştırın.
4. Takma kod, kurgusal ya da izinli alıntı ve tema adlarını girin. Birden çok temayı virgülle ayırın.
5. Alıntıda tanıtıcı bilgi varsa, uygulamanın sorduğu adımda maskeleyip düzeltilmiş metni girin.
6. İş bitince `kodlama_kayitlari.csv` dosyası aynı klasöre eklenir. Uygulama yeni oturumların kayıtlarını bu dosyaya ekler.

Kodlama mantığını kontrol etmek için `python3 -m unittest -v test_uygulama.py` komutunu çalıştırın. Program yalnızca Python standart kütüphanesini kullanır; class içermez.

## Özellikler

- Takma kod, alıntı ve tema girişlerini doğrular; boş veya biçimi geçersiz kaydı eklemez.
- Tanıtıcı bilgi bulunup bulunmadığını kullanıcıya sorar. Bulunuyorsa kullanıcıdan maskeleme ister; bunu kendi başına tespit etmez.
- Bir alıntıda bir veya birden fazla tema saklar.
- Başta/sonda boşlukları kaldırır, Türkçe büyük I/İ farklarını karşılaştırmada ele alır ve aynı alıntı içindeki yinelenen tema etiketini bir kez sayar.
- Yeni temayı 1'den başlatır; sonraki alıntılarda sayıyı artırır.
- CSV dosyasına kayıt satırlarını ve tema toplamlarını ekler.

## Gerçek test sonuçları

| Senaryo ve girdi | Beklenen | Gerçek sonuç |
|---|---|---|
| `P01`, dolu alıntı, `Eğitim` | Kayıt eklenir; tema 1 olur | Başarılı; `eğitim: 1` |
| Var olan temaya ` eğitim ` ve `EĞİTİM` | Boşluk/harf farkı birleştirilir, aynı alıntı bir kez sayılır | İlk denemede test başarısız oldu; Türkçe I/İ düzeltmesinden sonra beklenen sonuç alındı |
| `Eğitim` ve `Eşitsizlik` | İki farklı tema da 1 olur | Başarılı; iki sayaç da 1 |
| Boş alıntı | Kayıt ve sayaç değişmez | Başarılı; kayıt eklenmedi |
| Tanıtıcı bilgi var, maskelenmiş metin yok | Kayıt eklenmez | Başarılı; kayıt eklenmedi |
| Takma kod `Gerçek Ad` | Geçersiz takma kod reddedilir | Başarılı; kayıt eklenmedi |
| Tanıtıcı ayrıntı `[KİŞİ]`, `[YER]` olarak maskeli | Maskeli alıntı saklanır | Başarılı |
| CSV kaydı | Kayıt ve tema toplamı satırları yazılır | Başarılı; geçici CSV okundu |

Son düzeltmeden sonra test paketi **8/8 başarılı** oldu. İlk çalıştırmada Türkçe `İ` harfi nedeniyle bir test başarısız olmuştu; gerçek bulgu ve düzeltme `PROMPTLAR.md` içinde açıklanıyor.

## Gerçek terminal çıktısı

`examples/terminal_output.txt`, uygulamanın kurgusal bir girdiyle gerçek çalıştırmasından alınan çıktıdır. `examples/terminal_preview.png`, bu metinden oluşturulmuş bir görseldir; gerçek ekran fotoğrafı değildir.

## Dosyalar

- `uygulama.py` — uygulama
- `test_uygulama.py` — sekiz gerçek test
- `akis_semasi.png` — algoritma akış şeması
- `PROMPTLAR.md` — beş gerçek istem, AI yanıt özeti, kararlar, gerekçeler ve düzeltme kaydı
- `examples/terminal_output.txt` — gerçek çalıştırma çıktısı
- `examples/terminal_preview.png` — terminal çıktısının görsel sunumu
- `examples/kurgusal_ornek.csv` — örnek CSV çıktısı; yalnızca kurgusal veri içerir
