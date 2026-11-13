# Prompt günlüğü

Bu günlük yalnızca konuşmada gerçekten gönderilen istemleri, alınan yanıtların özetini ve onaylanan kararları içerir. Test hatası da gerçek Python çalıştırmasının çıktısına dayanır.

## Prompt 1 — İlk sözde kod incelemesi

**İstemim**

> Sosyologların görüşme alıntılarını temalara göre kaydetmesi için hazırladığım sözde kod taslağını incele. Taslağı düzeltip yeniden yazma. Yalnızca mantıksal eksik veya hataları, olası bir uç durumu ve bunların neden sorun olacağını belirt. Özellikle döngünün nasıl sona ereceğini ve ilk kez karşılaşılan bir temanın sayımının doğru başlayıp başlamadığını kontrol et.
>
> BAŞLA  
> Tema sayılarını tutmak için boş bir liste oluştur.  
> HER görüşme alıntısı için:  
> 　 Katılımcının takma kodunu, alıntıyı ve temayı al.  
> 　 EĞER alıntı veya tema boşsa: eksik bilgi mesajı göster.  
> 　 DEĞİLSE: alıntıyı takma kodu ve temasıyla kaydet; temanın sayısını bir artır.  
> 　 Kullanıcı yeni alıntı girmek istemiyorsa döngüyü bitir.  
> Kayıtları ve her temanın toplam sayısını göster.  
> Kayıtları bir dosyaya yaz.  
> BİTİR

**YZ ne yaptı?** Döngünün bitiş koşulunun belirsiz olduğunu, boş sayım tablosunda ilk temanın nasıl başlatılmadığını ve eksik girdide kayıt akışının tanımlanmadığını belirtti.

**Benim kararım ve gerekçem** A: Yeni temaları ilk görüldüğünde saymaya başlatıp her denemeden sonra devam sorusu sormak. Onaylanan gerekçe: Görüşmelerde yeni temalar ortaya çıkabilir; ilk temayı 1'den başlatmak ve devam sorusu sayımı ve döngünün bitişini açık kılar.

**Uygulanan değişiklik** Eksik kayıt atlanıyor; yeni tema 1 ile oluşturuluyor; devam sorusu her denemeden sonra geliyor.

## Prompt 2 — Gizlilik kontrolü

**İstemim**

> Bu algoritma katılımcı takma kodunu ve görüşme alıntısını kaydediyor. Alıntının içinde bir kişiyi tanıtabilecek bilgi bulunursa ne tür gizlilik riski oluşabilir? Bu riski azaltacak tek bir basit önlem öner. Algoritmayı baştan yazma; örneğini tamamen kurgusal tut ve gerçek kişi bilgisi kullanma.

**YZ ne yaptı?** Takma kodun tek başına yeterli olmadığını; alıntıdaki benzersiz rol, yer veya olay ayrıntılarının katılımcıyı tanıtabilir olduğunu açıkladı. Kaydetmeden önce bu ayrıntıları gözden geçirip maskeleme önerdi.

**Benim kararım ve gerekçem** A: Doğrudan alıntıyı koruyup tanıtıcı ayrıntıları kayıttan önce maskelemek. Onaylanan gerekçe: Doğrudan alıntılar araştırma temasını anlamaya yardım eder; tanıtıcı ayrıntıları kontrol edip maskelemek kimliği korumaya destek olur.

**Uygulanan değişiklik** Akışa alıntıyı tanıtıcı ayrıntılar açısından gözden geçirme adımı eklendi. Uygulama bu kontrolü otomatik yapmadığı için kullanıcıdan açıkça yanıt ve gerekirse maskelenmiş metin ister.

## Prompt 3 — Bağımsız algoritma ve olası hata

**İstemim**

> Sosyologların görüşme alıntılarını temalara göre kaydedip tema sayılarını çıkarması için, aşağıdaki taslaktan bağımsız, basit bir algoritma öner. Girdi, işlem ve çıktıyı belirt; en az bir karar ve bir döngü kullan. Python kodu yazma. Algoritmanın yanlış veya eksik sonuç verebileceği bir kurgusal durum da örnekle. Gerçek kişi bilgisi kullanma.
>
> Mevcut taslağım: Her kayıt için takma kod, alıntı ve tema alınıyor. Alıntı veya tema boşsa kayıt atlanıyor. Aksi hâlde alıntıdaki tanıtıcı ayrıntılar gözden geçirilip maskeleniyor, kayıt saklanıyor ve tema sayısı artırılıyor; yeni tema 1'den başlıyor. Kullanıcı devam etmek istemediğinde döngü bitiyor. Sonunda kayıtlar ve tema sayıları gösterilip dosyaya yazılıyor.

**YZ ne yaptı?** Başta kayıt sayısını alıp o kadar kez giriş yapan bağımsız bir algoritma önerdi. Her kayıt için tek ana tema seçmesi nedeniyle bir alıntının iki temayı içerdiği kurgusal durumda ikinci temanın sayımının düşük kalabileceğini belirtti.

**Benim kararım ve gerekçem** A: Bir alıntıya birden fazla tema atanabilsin. Onaylanan gerekçe: Bir alıntı birden fazla sosyolojik temayla ilgili olabilir; çoklu etiketler alıntının içeriğini daha eksiksiz yansıtır.

**Uygulanan değişiklik** Bir alıntı bir kez kaydediliyor; her farklı tema kendi sayacına bir kez ekleniyor.

## Prompt 4 — Tema adlarını karşılaştırma

**İstemim**

> Bir alıntıya birden fazla tema verilebilen algoritmada, tema adlarının başında/sonunda boşluk olması veya büyük-küçük harf farkı (“Eğitim” ve “ eğitim ” gibi) aynı temanın sayımını bölebilir mi? Bunu önlemek için basit ve tutarlı bir kural öner. Python kodu yazma ve algoritmayı baştan yazma.

**YZ ne yaptı?** Yazım farklarının aynı temayı ayrı saydırabileceğini söyledi; baştaki/sondaki boşlukları kaldırmayı ve karşılaştırmada harf büyüklüğünü yok saymayı önerdi.

**Benim kararım ve gerekçem** A: Tema adlarını otomatik normalleştir. Onaylanan gerekçe: Yeni tema ekleme esnekliği korunurken boşluk ve harf büyüklüğünden kaynaklanan ayrı sayımlar önlenir.

**Uygulanan değişiklik** Tema adları kırpılıyor, Türkçe I/İ dönüşümü dahil karşılaştırma anahtarıyla eşleniyor ve aynı alıntıdaki yinelenen etiket bir kez sayılıyor.

**Gerçek test bulgusu ve düzeltme** İlk gerçek test çalıştırmasında Python `casefold()` kullanımı Türkçe büyük `İ` harfini beklenenden farklı biçimde dönüştürdü; `Eğitim`, ` eğitim ` ve `EĞİTİM` aynı alıntıda tek tema olarak kalmadı. `theme_key()` işlevi NFC normalizasyonu ve Türkçe `I`/`İ` eşlemesiyle düzeltildi. Aynı senaryo tekrar çalıştırıldığında geçti; son test paketi 8/8 başarılı oldu.

## Prompt 5 — Akış şeması kontrolü

**İstemim**

> Aşağıdaki sosyoloji algoritmasına uygun bir Mermaid akış şeması oluştur. Başla/bitir, girdi/çıktı, işlem ve karar adımlarını standart akış şeması şekilleriyle göster. Her kararın Evet/Hayır çıkışını etiketle; devam sorusunun döngüye dönüşünü açıkça çiz. Şemayı algoritmaya göre oluştur, algoritmayı değiştirme. Gerçek kişi bilgisi kullanma.
>
> Algoritma: Takma kodu, görüşme alıntısını ve bir veya daha fazla temayı al. Takma kod, alıntı veya tema eksikse kaydı atla. Değilse alıntıdaki tanıtıcı ayrıntıları gözden geçirip maskele. Tema adlarında baştaki ve sondaki boşlukları kaldır, harf büyüklüğü farkını yok say ve aynı tema adını aynı alıntıda bir kez say. Alıntıyı temalarıyla kaydet. Her farklı tema daha önce sayılmışsa sayısını bir artır; yeniyse sayımını 1'den başlat. Kullanıcı yeni kayıt eklemek istemediğinde döngüyü bitir. Sonunda kayıtları ve tema sayılarını göster.
>
> Bir kararın veya döngünün şemada açıkça gösterilemediğini fark edersen, Mermaid kodundan sonra belirt.

**YZ ne yaptı?** Evet/Hayır dalları ve döngü dönüşü olan Mermaid şeması oluşturdu. Gizlilik adımının algoritmada karar koşulu olarak tanımlanmadığını; eksik kayıt sonrasında devam sorusunun nasıl uygulanacağının açık olmadığını belirtti.

**Benim kararım ve gerekçem** B: Gizlilik kontrolünü “Tanıtıcı bilgi var mı?” kararına çevirmek. Onaylanan gerekçe: Bilgi varsa maskeleme, yoksa doğrudan kaydetme adımlarını ve her denemeden sonra devam sorusunu açık kılar.

**Uygulanan değişiklik** Son akış şemasında gizlilik için Evet/Hayır kararı, eksik kayıtlar dahil her giriş denemesinden sonra devam kararı yer alıyor.

## Kaynak

OpenAI. (2026). ChatGPT [Büyük dil modeli]. https://chatgpt.com
