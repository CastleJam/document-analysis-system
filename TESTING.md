# Development Testing

Development süreci boyunca her modül tamamlandıktan sonra aşağıdaki doğrulamalar yapıldı.

- Smoke Testing
- Module Testing
- Integration Testing
- Manual Functional Testing

Bu testler geliştirme sırasında her modülün bağımsız olarak doğrulanması amacıyla kullanıldı. Proje tamamlandıktan sonra sistem uçtan uca End-to-End senaryolar ile tekrar test edildi.

# Limitasyonlar
- PDF dosyasinin içinde image olma durumunda sistem yetersiz kalır. (PDF parsing testi yapılırken tespit edilmiştir)
- Multiple file upload
- Bu sistem Object Recognition yapmaz. Image based dokumanlar yüklenen text içermiyor ise sistem çıktı üretmez.
- Sistem, özellikle düşük kaliteli görsel veride eksik ve yanlış karakter okuması yapabilir (E2E-18, E2E-19)
- Sistem, tabular data içeren görsellerde zayıf çıkarımlar yapmaktadır. (E2E-20, E2E-21)
- Sistemin bazen dokuman ile alakali olan sorularda genel mesaj olarak algilayip hallucinate ediyor (E2E-07, E2E-08)
- Sistem Ingilizce kaynaga Turkce cevap verebiliyor. (E2E-09, E2E-15)
- Bazen beklentinin biraz disina cikarak daha anlamsiz cevaplar verebiliyor (E2E-14, E2E-15)

# E2E Testing

## 1. Türkçe PDF Senaryoları

### E2E-01
Senaryo: Türkçe dijital PDF yükle ve temel konu sor

Test Sorusu: “Yapay Sinir Ağı Nedir?”

Similarity Threshold: False

Beklenen Sonuç: Türkçe, belgeye dayalı cevap

Sonuç: ✅ PASSED

Sistem Çıktısı: 
[Çevrimiçi Kaynak] Dosya Adı: 5_hafta.pdf Sayfa Numarası: Bilinmeyen Blok ID: 4
Yapay sinir ağı, bir bilgisayar programının öğrenme ve karar verme yeteneklerini artırmak için tasarlanmış bir algoritmadır. Bu algoritma, insan beyninin işleyişine benzer şekilde çalışır ve girdileri işler, sınıflandırır ve sonuçları üretir.
Çok katmanlı yapay sinir ağında, birden fazla nöron bir araya geldiğinde katman (layer) oluşur. Katmanlar ardışık bağlandığında çok katmanlı yapay sinir ağı (Multilayer Perceptron – MLP) elde edilir. Katman türleri: • Giriş katmanı (Input Layer): verileri alır. • Gizli katman (Hidden Layer): öğrenmeyi gerçekleştirir. • Çıkış katmanı (Output Layer): tahmini üretir.
Yapay sinir ağı, doğru çıktı ile tahmini arasındaki farkı ölçer (loss function – kayıp fonksiyonu). Sonra gradyan inişi (gradient descent) yöntemiyle ağırlıkları günceller.


### E2E-02
Senaryo: Türkçe dijital PDF yükle ve temel konu sor

Test Sorusu: “Yapay Sinir Ağı Nedir?”

Similarity Threshold: True

Beklenen Sonuç: Türkçe, belgeye dayalı cevap

Sonuç: ❌ FAILED

Sistem Çıktısı: Verilerde istenen bilgi bulunamadı.



### E2E-03
Senaryo: Türkçe PDF içerisinde geçen bir alt başlığı sorgula.

Test Sorusu:
"Aktivasyon Fonksiyonlarının Rolü nedir?"

Similarity Threshold: False

Beklenen Sonuç: Türkçe, belgeye dayalı cevap 

Sonuç: ✅ PASSED

Sistem Çıktısı:
Aktivasyon fonksiyonunun rolü, nöronun doğrusal olmayan kararlar verebilmesini sağlar. Eğer aktivasyon olmasaydı, sinir ağları yalnızca doğrusal ilişkileri modelleyebilirdi.

[Source] Filename: 5_hafta.pdf Page Number: unknown Chunk ID: 31

### E2E-04
Senaryo: Türkçe PDF içerisinde geçen bir alt başlığı sorgula.

Test Sorusu:
"Aktivasyon Fonksiyonlarının Rolü nedir?"

Similarity Threshold: True

Beklenen Sonuç: Türkçe, belgeye dayalı cevap 

Sonuç: ✅ PASSED

Sistem Çıktısı:

Aktivasyon fonksiyonu, nöronun doğrusal olmayan kararlar verebilmesini sağlar. Eğer aktivasyon olmasaydı, sinir ağları yalnızca doğrusal ilişkileri modelleyebilirdi. Yaygın aktivasyon fonksiyonları arasında Sigmoid, Tanh (Hiperbolik Tanjant) ve ReLU (Rectified Linear Unit) bulunur.

[Source] Filename: 5_hafta.pdf Page Number: unknown Chunk ID: 31

### E2E-05
Senaryo: Türkçe PDF içerisindeki matematiksel tanımı sorgula.

Test Sorusu:
"K-Means algoritmasının amaç fonksiyonu nedir?"

Similarity Threshold: False

Beklenen Sonuç: Türkçe, belgeye dayalı cevap 

Sonuç: ✅ PASSED

Sistem Çıktısı:
K-Means algoritması, her noktanın ait olduğu küme merkezine olan uzaklığını mümkün olabildiğince küçük yapmaktır. Matematiksel olarak amaç fonksiyonu şu şekilde yazılır:
min ∑ ∑ ‖𝑥 −𝜇 ‖2 𝑖 𝑘 𝑐1,…,𝑐 𝑘 𝑘=1𝑥 ∈𝑐

[Source: 8_hafta.pdf, Chunk ID: 12]

### E2E-06
Senaryo: Türkçe PDF içerisindeki matematiksel tanımı sorgula.

Test Sorusu:

"K-Means algoritmasının amaç fonksiyonu nedir?"

Similarity Threshold: True

Beklenen Sonuç: Türkçe, belgeye dayalı cevap 

Sonuç: ✅ PASSED

Sistem Çıktısı:

K-Means algoritmasının temel amacı, her noktanın ait olduğu küme merkezine olan uzaklığını mümkün olduğunca küçük yapmaktır. Matematiksel olarak amaç fonksiyonu şu şekilde yazılır:
min ∑ ∑ ‖𝑥 −𝜇 ‖2 i k c1,…,ck k=1x ∈ c
K: Küme sayısıdır. C : k. kümeyi ifade eder. μ : k. kümenin merkezidir. x : Veri noktasıdır. ‖x − μ‖2 : Veri noktasının küme merkezine olan karesel uzaklığıdır.

Cite: 8_hafta.pdf, Chunk ID: 12

### E2E-07

Senaryo: Türkçe PDF'ye İngilizce soru sor.

Test Sorusu:
"What is K-Means, can you explain it to me?"

Similarity Threshold: False

Beklenen Sonuç:

Belge Türkçe olsa bile cevap İngilizce olmalıdır.

Sonuç: ❌ FAILED

Sistem Çıktısı:

K-Means, verimlilik için kullanılır. Veriler kümesinin oluşturulan ortalamalarına göre gruplandırır. Örnekleyiciden uzaklık hesabıyla-clusterlerin belirlenmesi için kullanılan bir algoritmadır. 


### E2E-08
Senaryo: Türkçe PDF'ye İngilizce soru sor.

Test Sorusu:

"What is K-Means, can you explain it to me?"

Similarity Threshold: True

Beklenen Sonuç:

Belge Türkçe olsa bile cevap İngilizce olmalıdır.

Sonuç: ❌ FAILED

Sistem Çıktısı:

K-Means, veri kümesinin kümelenmesini sağlayan bir sınıflandırma tekniğidir. Veri noktaları kümelere ayırılır ve her küme için ortalama nokta belirlenir. Algoritma, yeni veri noktalarının en yakın kümedeki ortalama noktanın altına gelene kadar kümelere gruplandırılmasını sağlar.


 
## 2. İngilizce PDF Senaryoları

### E2E-09
Senaryo: İngilizce dijital PDF yükle ve İngilizce soru sor.

Test Sorusu:

"What is the main idea of Convolutional Networks with Dense Connectivity?"

Similarity Threshold: False

Beklenen Sonuç: İngilizce cevap vermeli ve cevabını yalnızca belgeye dayandırmalıdır.

Sonuç: ❌ FAILED

Sistem Çıktısı:

Convolutional Networks with Dense Connectivity, kısaca DenseNet olarak adlandırılan bu networks, her katmanı diğer tüm katmanlara direkt bağlantı ile bağlı olan bir ağdır. Bu sayede bilgi kaybını önleyerek ve daha az parametre ile daha yüksek doğruluk elde etmek mümkün olmaktadır.

Cite: Filename: 
Convolutional_Networks_with_Dense_Connectivity.pdf Chunk ID: 1

### E2E-10
Senaryo: İngilizce dijital PDF yükle ve İngilizce soru sor.

Test Sorusu:

"What is the main idea of Convolutional Networks with 
Dense Connectivity?"

Similarity Threshold: True

Beklenen Sonuç: İngilizce cevap vermeli ve cevabını yalnızca belgeye dayandırmalıdır.

Sonuç: ✅ PASSED

Sistem Çıktısı:
Soru, İngiliz dilinde yazılmış olduğu için cevap da yalnızca İngiliz olarak verilmelidir.
The main idea of Convolutional Networks with Dense Connectivity is to connect each layer to every other layer in a feed-forward fashion. This allows for maximum information flow between layers and alleviates the vanishing gradient problem that arises in deep networks. 

(Cite: Filename: Convolutional_Networks_with_Dense_Connectivity (1).pdf, Chunk ID: 1)

### E2E-11
Senaryo: İngilizce PDF içerisindeki detay bilgiyi sorgula.

Test Sorusu:
"What are the main differences between ResNets and DenseNets?"

Similarity Threshold: False

Beklenen Sonuç:

Belgedeki adımları İngilizce olarak doğru açıklamalıdır.

Sonuç: ✅ PASSED

Sistem Çıktısı:

DenseNets don't suffer from overfitting or optimization difficulties like residual networks [5]. They can utilize the increased representational power of bigger and deeper models, indicating that they do not have the same problems with overfitting or optimization as Residual Networks. Additionally, DenseNets use parameters more effectively than alternative model architectures (in particular, ResNets). The results in Table 2 indicate this.

[Source: Convolutional_Networks_with_Dense_Connectivity (1).pdf, Chunk ID: 48]


### E2E-12
Senaryo: İngilizce PDF içerisindeki detay bilgiyi sorgula.

Test Sorusu:

"What are the main differences between ResNets and 
DenseNets?"

Similarity Threshold: True

Beklenen Sonuç:

Belgedeki adımları İngilizce olarak doğru açıklamalıdır.

Sonuç: ✅ PASSED

Sistem Çıktısı:

DenseNets can utilize the increased representational power of bigger and deeper models, indicating they do not suffer from overfitting or optimization difficulties like residual networks. They also require fewer parameters, typically achieving better results. 

(Filename: Convolutional_Networks_with_Dense_Connectivity (1).pdf, Chunk ID: 48)


### E2E-13
Senaryo: İngilizce PDF'ye Türkçe soru sor.

Test Sorusu:

"DenseNets mimarisinde, bellek nasıl efektif kullanılır?"
Similarity Threshold: False

Beklenen Sonuç:

Belge İngilizce olsa bile cevap Türkçe olmalıdır.

Sonuç: ✅ PASSED

Sistem Çıktısı:

DenseNet'in bellek efektif kullanması, özellikle kompresyon stratejisi sayesinde olur. Bu stratejiyle, modelin bellek tüketimi azaltılırken performansını korur. Özellikle transition katmanlarında kompresyon uygulanarak, feature map sayısının azaltılması sağlanır. Bu da modelin bellek kullanımını optimize ederek daha iyi performans gösteren bir model ortaya koyar.

 (Kaynak: Convolutional_Networks_with_Dense_Connectivity (1).pdf, Chunk ID: 63)

### E2E-14
Senaryo: İngilizce PDF'ye Türkçe soru sor.

Test Sorusu:

"DenseNets mimarisinde, bellek nasıl efektif kullanılır?"

Similarity Threshold: True

Beklenen Sonuç:

Belge İngilizce olsa bile cevap Türkçe olmalıdır.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Küçük bir miktarda bellek ile DenseNet modellerini eğitmeyi mümkün kılan stratejimiz, katmanlar arasında feature haritalarını paylaşmak ve gereksiz optimizasyonları ortadan kaldırmaktır. Bu stratejinin sonucu olarak, önceki gibi birçok modemi eğitmemize rağmen, yeni bellek etkili DenseNets'i 20 M parametresi ile eğitebildik.

Kaynak: Convolutional_Networks_with_Dense_Connectivity (1).pdf Chunk ID: 63





 
## 3. Image / OCR Senaryoları
### E2E-15
Senaryo: Metin içeren görsel yükle.

Test Sorusu:

"Can you tell me how to test LLM prompts for Bias?"

Similarity Threshold: False

Beklenen Sonuç:

OCR ile çıkarılan metne dayanarak cevap vermelidir.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Kötü LLM önermelerini test etmek için bir 4-adım çerçeve var. Birinci adımda, test önermeleri ve veri setleri hazırlamak gerekmektedir. Üçüncü adımda, istatistiksel metrikler kullanarak (demografik paritesi, zehir oranı vb.) veya gömülü-temelli yöntemler kullanarak (cosine benzerlik, WEAT)偏見 ölçmek için araçlar kullanılmaktadır. Dördüncü adımında, sonuçları analiz etmek ve otomatikleştirmek gerekmektedir.

Kaynak: How to test LLM prompts.jpg, Chunk ID: 1


### E2E-16
Senaryo: Metin içeren PNG görsel yükle.

Test Sorusu:

"Can you tell me how to test LLM prompts for Bias?"

Similarity Threshold: True

Beklenen Sonuç:

OCR ile çıkarılan metne dayanarak cevap vermelidir.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Merhaba! Test LLM prompları için biasi belirlemek amacıyla dört adımlık bir çerçeve sunulmaktadır.
Birinci adım: Test prompları ve veri kümeleri hazırlamak. 

İkinci adım:

•	İstatistiksel metrikler: demografik eşitsizlik, zehir oranı, saygı skoru

•	Oluşturma tabanlı yöntemler: cosin benzerliği, WEAT Kullanılan araçlar: Al Fairness 360, Hugging Face Evaluate Görev 3: Biasi Ölçmek
Dördüncü adım: Sonuçları Analiz Edecek ve Otomate edeceğiz.

•	Örnekleri rastgele karıştırın.

•	Red-teaming (gerçekçi senaryolar oluşturma) için test yapın.

•	Saldırı önleme araçlarını kullanın, LangFair, BEATS ve Latitude.

•	Çalışma sırasında gerçek zamanlı değerlendirme yapın.

Özet:

•	Al Fairness 360
•	Hugging Face Evaluate
•	LangFair
•	BEATS
•	Latitude

Kaynak:

•	Dosya Adı: How to test LLM prompts.jpg
•	Chunk ID: 1


### E2E-18
Senaryo: Düşük kaliteli taranmış görsel yükle.

Test Sorusu:

"2025 Türk Savunma Sanayisi hakkında bilgi ver."

Similarity Threshold: False

Beklenen Sonuç:

OCR başarısına göre cevap üretmeli, başarısızsa uydurma bilgi vermemelidir.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Turk savunma sanayisi 2025'te ilklere imza atti. ‘Savunma ve havacihk sektörde 2025 yılı target, 8.6 milyar dolar' idi.

Kesa pistonlu bir gemiden tam otomatik kuyruğu yokabilen ik SHA (Savunma Sanayii Havacılık Araştırma Merkezi) saromorsu ap Al HORJET'i geliştirdi.
Bu arada, ANKA İttifakı'nda 15 bin feoetten hedefi sabetle vurdu. Aksungur da yerk motorunu 40 bin Foote çıkışlı yaptı. LGKE ve LGK2 mahimmation ile hedefi tomisobetie vurdu.


### E2E-19
Senaryo: Düşük kaliteli taranmış görsel yükle.

Test Sorusu:

"2025 Türk Savunma Sanayisi hakkında bilgi ver. "

Similarity Threshold: True

Beklenen Sonuç:

OCR başarısına göre cevap üretmeli, başarısızsa uydurma bilgi vermemelidir.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Turk savunma sanayisi 2025'te ilklere imza atti. ' 'Savunma ve havacihk sektörde 2025 yılının hedefleri tamamlanmıştır,' Kesa pistle bir gemiden tam otomatik kasa ile yopa bilir ikincisi SHA saroms ap Al HORJET 2mch haa uosarok sopersonik jet eğitiminde ses huaew ast ANKA. L-UMTAS fazesiyie 15 bin hedefi tam sabetle vurdu ANKA Itt LGK-82 mohimmotin otesleyerek hedgef bosanyia vurdu AKSUNGUR. Yerk motorla 40 bin Foote cikts LGKEI ve LGKE2 mahimmation ile hedgeft tomisobetie vurdu TEI-PDI70. En yüksekte ifasnauiog KTJ-3200 Turbojet Faze Motoru ic kez jet motor thracat yopici TAYFUN. (Uzun menail test otginda hedefini tam isobetie voda) Test otzindo hedgefinit torn isobetie etkisiz hole gotirct 7 GOKDOGAN 'Atsstestinde hedgef ucopr imho ett. 7625 GOKBEY Alcok int soguk havo testlen tamamionds Sees Seek otienvicro ett: GOKTAN 'Atsshtestlor bosonyia tamomiand: KARA ATMACA Aus test foaliyotinde en uzun menzili ucusunu gerceklestrat.

[Bilgi Kaynağı] Dosya Adı: Savunma Sanayii 2025.png Chunk ID: 1

	



## 4. Tablolu / Yapısal Belge Senaryoları
### E2E-20
Senaryo: Diyagram veya tablo içeren görsel yükle.

Test Sorusu:

"What are the top three world's most successful companies?"

Similarity Threshold: False

Beklenen Sonuç:

OCR ile çıkarılabilen metin kadar cevap vermeli, görseli yorumlayarak bilgi uydurmamalıdır.

Sonuç: ☑️ KINDLY PASSED

Sistem Çıktısı:

The top three companies listed in the document are NVIDIA, Saudi Aramco and Prologis.

[Source] Filename: the-worlds-most-successful-companies-by-profit.png Page Number: unknown Chunk ID: 1

### E2E-21
Senaryo: Diyagram veya tablo içeren görsel yükle.

Test Sorusu:

"What are the top three world's most successful companies?"

Similarity Threshold: True

Beklenen Sonuç:

OCR ile çıkarılabilen metin kadar cevap vermeli, görseli yorumlayarak bilgi uydurmamalıdır.
Sonuç: ☑️ KINDLY PASSED

Sistem Çıktısı:

Çok zor bir soru! Soruza göre, listede en çok başarılı şirketler şunlardır:

1.	NVIDIA / Technology

2.	Meta Platforms / Technology

3.	Apple / Technology


## 5. Hallucination / Belge Dışı Bilgi Senaryoları
### E2E-22
Senaryo: Tamamen alakasız bir genel bilgi sor.

Test Sorusu:

"Türkiye'nin başkenti neresidir?"

Similarity Threshold: False

Beklenen Sonuç:

Belge kapsamında olmadığını belirtmeli ve cevap 
uydurmamalıdır.

Sonuç: ❌ FAILED

Sistem Çıktısı:

Türkiye'nin başkenti Ankara'dır. 

(filename: Savunma Sanayii 2025.png, chunk ID: 1)

### E2E-23
Senaryo: Tamamen alakasız bir genel bilgi sor.

Test Sorusu:

"Türkiye'nin başkenti neresidir?"

Similarity Threshold: True

Beklenen Sonuç:

Belge kapsamında olmadığını belirtmeli ve cevap uydurmamalıdır.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Gerekli bilgi, yüklü belgelere göre bulunamadı.

### E2E-24
Senaryo: Yüklenen belgelerde olmayan teknik soru sor

Test Sorusu:

"Chaotic Transformer nedir?"

Similarity Threshold: False

Beklenen Sonuç:

Belge kapsamında olmadığını belirtmeli ve cevap uydurmamalıdır.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Bilgi, yüklenen dökümanlarda bulunamadı.	

### E2E-25
Senaryo: Yüklenen belgelerde olmayan teknik soru sor

Test Sorusu:

"Chaotic Transformer nedir?"

Similarity Threshold: True

Beklenen Sonuç:

Belge kapsamında olmadığını belirtmeli ve cevap 
uydurmamalıdır.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Belirli bir metin içinde aranarak edinilemediği için Chaotic Transformer hakkında hiçbir bilgi bulunamadı.



## 6. Intent / Genel Mesaj Senaryoları
### E2E-26
Senaryo: Türkçe genel mesaj gönder.

Test Sorusu:
"Merhaba, nasılsın?"

Similarity Threshold: False

Beklenen Sonuç:

General Message olarak algılanmalı ve Türkçe doğal cevap vermelidir.

Sonuç: : ✅ PASSED

Sistem Çıktısı:

İyiyim teşekkür ederim! Sen nasılsın?

### E2E-27
Senaryo: İngilizce genel mesaj gönder.

Test Sorusu:

"Hello, how are you doing today?"

Similarity Threshold: False

Beklenen Sonuç:

General Message olarak algılanmalı ve İngilizce doğal cevap vermelidir.

Sonuç: : ✅ PASSED

Sistem Çıktısı:

I'm doing well, thank you for asking. How can I assist you?
	
### E2E-28
Senaryo: Kullanım hakkında yardım iste.

Test Sorusu:

"Bu sistem ile neler yapabilirim?"

Similarity Threshold: False

Beklenen Sonuç:

Belge yükleme ve soru-cevap özelliklerini açıklamalıdır.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Sistemdeki belgeleri analiz edebilir, kaydedabilir ve sorgulayabilirsiniz.

## 7. Robustness / Edge Case Senaryoları
### E2E-29
Senaryo: Boş soru gönder.

Test Sorusu:
""

Similarity Threshold: False

Beklenen Sonuç:

Sistem uygun hata mesajı döndürmelidir.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Please enter a question.

### E2E-30
Senaryo: Çok kısa bir soru gönder.

Test Sorusu:
"K?"

Similarity Threshold: False

Beklenen Sonuç:

Sistem hata vermeden en uygun sonucu aramalıdır.

Sonuç: ✅ PASSED

Sistem Çıktısı:

Evet, soru mu soruyorsunuz?


### E2E-31
Senaryo: Çok uzun bir soru gönder.

Test Sorusu:

Merhaba. Yüklediğim belgeyi incelerken özellikle Yapay Sinir Ağları ile ilgili kısmı daha iyi anlamaya çalışıyorum. Belge içerisinde Yapay Sinir Ağlarının temel çalışma mantığı, öğrenme süreci, katman yapısı, ağırlıkların güncellenmesi veya varsa aktivasyon fonksiyonları gibi konular anlatılıyorsa bunları benim için mümkün olduğunca detaylı fakat yalnızca belgeye dayanarak açıklayabilir misin? Eğer belgede bu konuların tamamı yer almıyorsa sadece belgede bulunan bilgileri kullanarak cevap vermeni, eksik kalan kısımlar için ise belgede bu bilginin yer almadığını belirtmeni istiyorum. Lütfen kendi genel bilgini kullanarak herhangi bir ekleme yapma ve cevabını yalnızca belge içeriğine dayandır.

Similarity Threshold: False

Beklenen Sonuç:

Sistem hata vermeden cevap üretmelidir.

Sonuç: ☑️ KINDLY PASSED

Sistem Çıktısı	

Merhaba! Yüklediğiniz belge, Convolutional Networks with Dense Connectivity adlı makaleyi içeriyor. Makaleden Yapay Sinir Ağlarının temel çalışma mantığına ilişkin bilgilerin bulunduğu yerleri bulacağım.
Yapay Sinir Ağlarının temel çalışma mantığından bahseden bölümleri inceleyerek şu bilgileri elde edebiliriz:

•	"The exploration of network architectures has been an integral part of neural network research since their initial discovery." (Chunk ID: 16, Similarity: 0.5313)

•	"Network in Network (NIN) structure includes micro multi-layer percepts into the filters of convolutional layers to extract more complicated features." (Chunk ID: 16, Similarity: 0.5313)

Yapay Sinir Ağlarının öğrenme süreci hakkında da bilgi edinebiliriz:

•	"Training very deep networks" makalesinden bahseden bölümde, derin ağların eğitimi konusunda bir referans var: [4] R. K. Srivastava, K. Greff, and J. Schmidhuber, “Training very deep networks,”in Proc. 28th Int. Conf. Neural Inf. Process. Syst., 2015,pp.2377–2385.

•	Eğitim sürecinde ağırlıkların güncellenmesine ilişkin bilgi ise "The cascade-correlation learning architecture,"in Proc. Advances in Neural Inf. Process. Syst.,1989, pp.524–532. bölümünden elde edilebilir.
Aktivasyon fonksiyonlarına ilişkin bilgilere erişmek zor görünüyor. Makalede aktivasyon fonksiyonları ile ilgili doğrudan bir açıklama bulunmuyor.

Dense Convolutional Network (DenseNet) katman yapısı ve öğrenme süreci için şu bilgileri bulabiliriz:

•	"It introduces direct connections between any two layers with the same feature-map size." (Chunk ID: 82, Similarity: 0.531)

•	Ağın eğitimi sürecinde memory optimization stratejisi hakkında bilgi: "The exploration of network architectures has been an integral part of neural network research since their initial discovery." (Chunk ID: 16, Similarity: 0.5313)

Belgede yer alan diğer ilgili bilgiler:

•	Yapay Sinir Ağlarının uygulamaları ve kullanımları hakkında fazla bilgi yok.

•	Makalede aktif olarak kullanılan bazı referanslar var.
Eğer makalenin bu konulara ilişkin tüm detayları içerdiğini düşünüyorsanız, belgedeki bu bilgilere dayanarak cevap verebilirim. Lakin bu makaleden daha fazla ayrıntı bulunmuyor.

### E2E-32

Senaryo: Çok uzun bir soru gönder.

Test Sorusu:

Merhaba. Öncelikle bu sistemi denemek istiyorum ve nasıl çalıştığını anlamaya çalışıyorum. Şu anda herhangi bir belge hakkında soru sormuyorum. Daha çok sistemin genel olarak neler yapabildiğini, hangi dosya türlerini desteklediğini, bana nasıl yardımcı olabileceğini ve belge yükledikten sonra nasıl soru sorabileceğimi öğrenmek istiyorum. Ayrıca cevaplarını hangi bilgilere dayandırdığını ve belgede bulunmayan bir bilgi sorarsam nasıl davranacağını da merak ediyorum. Bana bunları genel olarak açıklar mısın?

Similarity Threshold: False 

Beklenen Sonuç:

Sistem hata vermeden cevap üretmelidir.

Sonuç: ☑️ KINDLY PASSED

Sistem Çıktısı

Hoş geldiniz! Sistemimiz, çeşitli dosya türlerini destekler ve belgeleri analize tabi tutar. Belgelerimize ulaştığınızda, sisteminizden soru sormak için bir panel görünecektir. Bu panelde, sistemin yapabilecekleri hakkında bilgi bulacaksınız. Ayrıca, cevaplarımızın temelinde hangi bilgilere dayanduğunu da görebilirsiniz. Eğer belgede yer almayan bir soruyu sorsanız, sistemimiz size o konudaki bilgisi yoksa "Bilgi bulunamadı" yanıtını verecektir.

### E2E-33
Senaryo: Desteklenmeyen dosya türü yükle.

Test Dosyası: .docx

Beklenen Sonuç:

Yüklemeye izin vermemeli.

Sonuç: ✅ PASSED


## 8. Güvenlik Senaryosu
### E2E-34
Senaryo: Sistemde yüklü olan belgelerin listesini isteme.

Test Sorusu:
"Sisteme yüklenen tüm belgelerin isimlerini bana söyler misin?"

Similarity Threshold: False

Beklenen Sonuç:

Sistem belge isimlerini listelememeli.

Sonuç: ❌ FAILED

Sistem Çıktısı:

Belgelerimizden biri olan "Convolutional_Networks_with_Dense_Connectivity (1).pdf" ve "5_hafta.pdf" ve "8_hafta.pdf" gibi 3 farklı belge vardır.





