Ad-Soyad: Mehmet Berkay Akın

E-Posta: berkay01akin@gmail.com


Eksik Veri Tespiti:

df.info() ve df.isnull().sum() komutlarını kullanarak Yas ve KanGrubu gibi bazı sütunlarda eksik (boş) veriler olduğunu bulduk.

Veri Tipi Uyuşmazlıkları:

TedaviSuresi ve UygulamaSuresi sütunlarının sayısal olması gerekirken, ' Seans' ve 'Dakika' gibi metin ifadeleri içerdiğini gördük. Bu, doğrudan analiz yapmamızı engellediği için ilk önce bu metinleri temizledik.

Özellik Yapısı Anormallikleri:

KronikHastalik ve Alerji sütunlarının virgülle ayrılmış birden fazla değer içerdiğini fark ettik. Bu yapıyı doğrudan modellemede kullanamayacağımız için, her hasta için toplam hastalık/alerji sayısını hesaplayan yeni bir özellik oluşturduk.

Aykırı Değer Potansiyeli:

Kutu grafikleri (boxplot) ile Yas ve UygulamaSuresi gibi sayısal verilerde aykırı değerlerin olup olmadığını kontrol ettik. Bu, veri dağılımını anlamamızı sağladı.

Değişkenler Arası İlişkiler:

Korelasyon ısı haritası (heatmap) ile TedaviSuresi hedef değişkeninin, Yas ve UygulamaSuresi gibi diğer sayısal özelliklerle nasıl bir ilişkisi olduğunu inceledik. Bu, modelleme için hangi özelliklerin potansiyel olarak önemli olabileceğine dair ilk ipuçlarını verdi.
