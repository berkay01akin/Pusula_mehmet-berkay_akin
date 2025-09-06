# Pusula_mehmet-berkay_akin
Ad-Soyad: Mehmet Berkay Akın

E-posta: berkay01akin@gmail.com

1. Projeye Genel Bakış
Bu proje, bir fiziksel tıp ve rehabilitasyon veri seti üzerinde gerçekleştirilen bir veri bilimi vaka çalışmasıdır. Amacımız, 2235 gözlem ve 13 özellikten oluşan bu veri setini kapsamlı bir şekilde keşfetmek (EDA) ve TedaviSuresi hedef değişkeni etrafında tahmine dayalı modelleme için hazır hale getirmektir. Bu süreçte, veri temizliği, özellik mühendisliği ve veri ön işleme gibi temel veri bilimi adımları uygulanmıştır.

2. Keşifçi Veri Analizi (EDA) Bulguları
Veri setini inceleyerek aşağıdaki ana bulgulara ulaştım:

Veri Seti Yapısı: Veri seti, 2235 satır ve 13 sütundan oluşmaktadır. Sütunlar, sayısal (Yas, TedaviSuresi, UygulamaSuresi) ve kategorik (Cinsiyet, KanGrubu, Bolum) olmak üzere iki ana tipe ayrılmaktadır.

Eksik Değerler: Yas ve KanGrubu sütunlarında eksik veriler tespit edilmiştir. Bu eksiklikler, ön işleme aşamasında ele alınmıştır.

Veri Tipi Uyuşmazlığı: Hedef değişken olan TedaviSuresi ve UygulamaSuresi sütunları, metin ifadeleri (' Seans', 'Dakika') içerdiği için sayısal olarak kullanılamaz durumdadır. Bu sütunlar, analiz ve modelleme öncesinde temizlenmiştir.

Önemli Özellikler: KronikHastalik ve Alerji sütunları, virgülle ayrılmış birden fazla değer içermektedir. Bu verilerden anlamlı bir bilgi çıkarmak için, her hasta için kronik hastalık ve alerji sayısını gösteren yeni özellikler türetilmiştir.

Korelasyon: TedaviSuresi ile diğer sayısal değişkenler arasında anlamlı bir korelasyon olup olmadığı incelenmiştir. İlk analizlerde, Yas ile TedaviSuresi arasında hafif pozitif bir ilişki gözlemlenmiştir.

3. Veri Ön İşleme Adımları
EDA bulgularına dayanarak, veriyi modellemeye hazır hale getirmek için aşağıdaki adımlar uygulanmıştır. Bu adımlar, kodun tekrar kullanılabilirliğini ve modülerliğini artırmak amacıyla bir pipeline yapısı içinde organize edilmiştir.

Veri Temizliği:

TedaviSuresi ve UygulamaSuresi sütunlarındaki metin ifadeleri temizlenerek sayısal veri tipine dönüştürülmüştür.

Özellik Mühendisliği (Feature Engineering):

KronikHastalik ve Alerji sütunlarındaki virgülle ayrılmış değerler sayılarak KronikHastalikSayisi ve AlerjiSayisi adında yeni sayısal özellikler oluşturulmuştur.

Eksik Değerlerin Ele Alınması:

Sayısal eksik değerler (Yas gibi) medyan (median) ile, kategorik eksik değerler ise en sık görülen değerle (most_frequent) doldurulmuştur.

Kategorik Değişkenlerin Kodlanması:

Cinsiyet, KanGrubu ve Bolum gibi kategorik değişkenler, makine öğrenmesi algoritmalarının anlayabileceği bir formata dönüştürülmek üzere One-Hot Encoding tekniğiyle kodlanmıştır.

Sayısal Verilerin Ölçeklendirilmesi:

Farklı birimlerdeki sayısal değişkenlerin (Yas, UygulamaSuresi, vb.) modele eşit etki etmesini sağlamak için StandardScaler kullanılarak standartlaştırılmıştır.

Bu adımlar, ColumnTransformer ve Pipeline kullanılarak, verinin tek bir komutla temizlenip dönüştürülmesini sağlayan modüler ve yeniden kullanılabilir bir yapı içinde düzenlenmiştir. Bu yaklaşım, farklı veri setlerine kolayca uygulanabilir ve projenin kalitesini artırır.

4. Kodun Çalıştırılması
Bu projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

Gerekli kütüphaneleri kurun:
pip install pandas scikit-learn matplotlib seaborn openpyxl

Talent_Academy_Case_DT_2025.xlsx dosyasını, Python betiğiyle aynı klasöre yerleştirin.

Yukarıdaki Python kodunu çalıştırın. Kod, EDA bulgularını ve işlenmiş verinin boyutunu konsola yazdıracaktır.
