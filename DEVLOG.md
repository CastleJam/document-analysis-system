# DEVLOG

## Problemi nasıl parçaladınız?

Problemi 4 framework'e ayırdım.

### 1. Arayüz / Kullanıcı Deneyimi

Kullanıcı belge yükleyecek, soru soracak, cevap görecek.

### 2. Belge İşleme

PDF'den metin çıkarma, resimden metin çıkarma, Türkçe/İngilizce destek.

### 3. Soru-Cevap Katmanı

Kullanıcının sorusunu belge içeriğine göre cevaplama, belgede yoksa "bilmiyorum" deme. Hallucinate etmeme. Genel mesaj tespiti.

### 4. Testing

Bu probleme, ilk olarak hangi şekilde MVP teslim edeceğimi düşünerek başladım: Terminal, Windows App veya Web App.

İlk aklıma gelen düşünce web application olması. Bunun için iki yöntemden birisini seçerim diye düşündüm: Java üzerinden Spring Boot framework'ünü kullanarak projenin backend'ini oluşturmak ya da Python kullanarak Flask veya FastAPI ile bir web application oluşturmak. Kritik karar noktası sorusunda buna cevap verildi.

Kullanıcının yüklediği dokümanların classified olma durumu veya KVKK'dan dolayı belli güvenlik önlemlerinin alınabileceği durumu değerlendirildi. Şimdilik projeye daha basit yaklaşmaya karar verdim, ama ilerisi için güvenlik protokollerini entegre etmek mantıklı olabilir; örneğin Login Based System, User Roles, Document Classification Levels – PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED.

Belge işleme framework'ü için lokalde çalıştırılabilecek bir LLM (örneğin Hugging Face'den veya Ollama'dan indirilen bir LLM) olabilir veya API bağlantısı kurularak (örneğin Google 2.5 Flash) LLM desteği sağlanabilir diye düşündüm. Bu aşamada henüz net bir karar vermedim. Kritik karar noktası sorusunda buna cevap verildi.

Bu projenin RAG ile alakalı olduğu değerlendirildi. Bunun için bana gerekli olacak araçlar, kütüphaneler, yöntemler, süreçler incelendi ve genel olarak şu kanıya varıldı:

* Document Processing
* Text Extraction
* Text Cleaning
* Chunking
* Embedding
* Vector Database
* LLM

Bunlar için kullanılacak olan yöntem ve kütüphaneler araştırıldı.

Bu MVP nezdinde önce bir System Architecture oluşturdum. Bu dokümana `docs/` direktörisinden erişebilirsiniz.

Problemi parçaladığım 4 framework'ü ve System Architecture'ı düşünerek bir Flow Chart oluşturdum. Bu diagram aslında oluşturduğum Flow Chart'ın ikinci ve final versiyonudur. Düşünce akışımdaki değişen kısım sadece "Threshold Check" kısmı oldu. Onun dışında hızlı ilerlemek için genel akışı bozmak istemedim. Bu dokümana `docs/` direktörisi üzerinden erişebilirsiniz.

---

# Kritik karar noktalarında hangi alternatifleri değerlendirdiniz?

Proje üzerinde tahmini çalışma süresi ve teslimat tarihi değerlendirildiğinde, görüntü işleme (OCR), PDF işleme, LLM entegrasyonu gibi modülleri bir bütün olarak düşündüğümde Python dili ile projeyi yazmaya karar verdim. Hızlı MVP geliştirme tarafında Python daha pratik. Java/Spring Boot daha kurumsal ve güçlü bir backend seçeneği olabilir ama 7 günlük ve 25–35 saatlik böyle bir MVP için Python daha hızlı sonuç verecektir diye düşündüm.

Projenin bir Web App MVP olmasına karar verdim. Terminal güzeldir, hızlıdır ama müşteri deneyimi açısından çok hoş durmayabilir. Windows App, Web App'e nazaran biraz daha karmaşık bir proje olabilir. Web App ise hem demo için iyi hem de kullanıcı belge yükleme/soru sorma akışına doğal olarak daha iyi uyacaktır düşüncesiyle bu yolu tercih ettim.

## Chunking seçimi

Chunking seçiminde Character Chunking, Sentence Chunking, Paragraph Chunking, Recursive Chunking ve Semantic Chunking yöntemlerini değerlendirdim. Recursive Chunking sektördeki best practicelerden birisi olduğu ve LangChain tarafında desteklendiği için seçilmiştir. Semantic Chunking güzel sonuç verecektir diye düşündüm ama onun için embedding model gerekecek ve daha fazla işlem maliyeti, debugging'e sebep olacaktır. Bu MVP için onu uygun görmedim.

Ayrıca bu MVP için 1000 karakter chunk size ve 300 karakter overlap seçtim. Bu değerler, küçük ve orta boy belgelerde anlam bütünlüğünü korurken retrieval maliyetini düşük tutmak için dengeli bir başlangıç noktası olacaktır diye düşündüm. Projenin ölçeklenmesi durumunda ileride optimize edilebilir.

## Embedding seçimi

Embedding yöntem en önemli karar noktalarından biriydi. Aşağıdaki değerlendirmeler ışığında `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` modeli tercih edildi.

* `all-MiniLM-L6-v2`, hafif, hızlı ve semantik arama görevlerinde yaygın olarak kullanılan bir model olduğu için değerlendirildi. Ancak ağırlıklı olarak İngilizce için optimize edilmiş olması, case study kapsamında istenen Türkçe ve İngilizce belge desteği açısından uygun görülmedi.
* `intfloat/multilingual-e5-small`, çok dilli yapısı ve retrieval odaklı tasarlanmış olması nedeniyle değerlendirmemde öne çıktı. Diğer embedding yöntemlerinden farklı olarak sorguların query ve dokümanların passage prefix'leriyle hazırlanmasını gerektireceği için tercih edilmedi.
* `BAAI/bge-m3`, güçlü çok dilli retrieval performansı sunan modern bir model olduğu için değerlendirildi. Ancak MVP ihtiyaçlarına göre daha büyük ve ağır bir model olması nedeniyle tercih edilmedi.
* OpenAI Embeddings, yüksek embedding kalitesi nedeniyle alternatifler arasında yer aldı. Ancak API bağımlılığı oluşturması, kullanım maliyeti getirmesi ve belge içeriklerinin dış bir servise gönderilmesini gerektirmesi nedeniyle veri güvenliği açısından tercih edilmedi.
* BERT tabanlı standart embedding yaklaşımı da değerlendirildi. Ancak BERT doğrudan cümle seviyesinde semantik arama için optimize edilmiş bir model olmadığı için bu MVP kapsamında uygun görülmedi.

Yapılan değerlendirmeler sonucunda `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` modeli tercih edildi. Modelin Türkçe ve İngilizce desteği sunması, tamamen local olarak çalışabilmesi, CPU üzerinde MVP geliştirme süreci için yeterince hafif olması, 384 boyutlu embedding üretebilmesi ve ChromaDB ile kolay entegre edilebilmesi nedeniyle bu proje için en dengeli çözüm olduğu değerlendirildi.

## Vector Database seçimi

Vector Database seçimi diğer bir kritik karar noktasıydı. Bunun için FAISS, ChromaDB ve Pinecone alternatifleri değerlendirildi.

* FAISS, küçük ve orta ölçekli projelerde yüksek performanslı ve hafif bir seçenek olarak değerlendirildi. Ancak metadata yönetimi ve kalıcı veri saklama tarafında ek geliştirme ihtiyacı doğurabileceği için MVP kapsamında ikinci planda bırakıldı.
* ChromaDB, Python tabanlı olması, RAG projelerinde yaygın kullanılması, local çalışabilmesi, kolay kurulum sunması ve chunk bazlı metadata tutabilmesi nedeniyle tercih edildi. Bu projede her chunk için dosya adı, dosya tipi, benzerlik oranı ve yükleme zamanı gibi metadata bilgilerini saklamak istedim. Bu nedenle ChromaDB, yalnızca vektör araması yapmakla kalmayıp belge takibi ve kaynak gösterme açısından da daha uygun bir seçenek olarak değerlendirildi.
* Pinecone ise ölçeklenebilir ve production-ready bir cloud vector database çözümü olarak değerlendirildi. Ancak ücretli olması, API bağımlılığı getirmesi ve belge verilerinin dış bir servise gönderilmesi nedeniyle MVP kapsamında tercih edilmedi.

## LLM seçimi

Soru-Cevap katmanında ise LLM seçimi olarak iki farklı yaklaşım değerlendirildi.

İlk yaklaşım, Google Gemini 2.5 Flash gibi API tabanlı bir LLM kullanmaktı. Bu yöntem güçlü bir model sunmasına rağmen iki temel sebepten dolayı tercih edilmedi.

* API tabanlı servisler belirli kullanım limitlerine ve maliyetlere sahiptir. MVP kapsamında ücretsiz kullanım yeterli olsa bile, gerçek kullanım senaryolarında sorgu sayısı arttıkça maliyet oluşacağı değerlendirildi.
* Savunma sanayii ve defans endüstrisi ile alakalı projelerde yüklenen belgelerin dış bir servise gönderilmesi veri güvenliği açısından uygun olmayabilir. Bu nedenle tamamen lokal çalışan bir LLM çözümünün daha doğru bir yaklaşım olacağı düşünüldü.

Bu minvalde, lokalde çalışan LLM kullanımına karar verildi. İlk olarak Google'ın Gemma 3.1 1B olan 32K context window'lu modeli kullanıldı. Daha sonra Meta'nın Llama 3.1 8B olan 128K context window'lu modeline geçildi.

---

# Hangi yaklaşımları denediniz? Hangisi işe yaramadı ve neden?

Karşılaşılan problemlerden birisi, LLM'in Türkçe soruya Türkçe, İngilizce soruya İngilizce cevap verirken kafasının karışması, öyle ki bazen Korece ifadeler sunduğu tespit edildi. Ayrıca "Nasılsın?" sorusunda genel bir mesaj olduğunu algılamak yerine RAG'a başvurması ve cevap olarak "I could not find it in the documents" gibi bir cevap veriyor olması iyi sonuçlar vermediğini ve adjustment gerekliliğini gösterdi. Bu durumda Google Gemma 1B küçük bir model olarak yetersiz kalmış olabilir diye düşündüm. Muadil olarak reasoning yapabilen Llama 3.1 8B entegre edildi. Sonuç olarak geliştirme sağlandı ve Llama 3.1 8B kullanımına karar verildi.

RAG'a gitme senaryolarında ChromaDB'den dönen chunk'ların similarity'sine bakıp, belirlenen bir threshold'a göre cevap verip vermeme yaklaşımı ile LLM'in kendisinin reasoning yapıp cevap verip vermemesini kendisine bırakmak yaklaşımları denendi. Threshold için tutarlı bir default value belirlemekte zorluk yaşadım. Örneğin bazı test senaryolarım için database'den dönen chunk'ların similarity'si 0.5 iken çok güzel ve alakalı cevaplar alabiliyordum. Ama threshold 0.4, 0.5 veya 0.6 gibi değerleri genellemek pek mümkün olmuyordu. Genelleme yapamamaktan ötürü reasoning yapan bir LLM seçmenin faydasını burada gördüm. RAG ile dönen chunk'ları LLM'in cevap olarak üretmesinde uygun bilgi olup olmadığını değerlendirmesini ve kesinlikle hallucinate etmemesini istedim.

Sorulan bir soru, kaynak dokümanda hangi dilde geçiyor ise cevabı o dilde veriyor olması probleminde takıldım. Prompt adjustment'lar yapsam da, daha iyi bir model tercih etsem de beklediğim çözüme maalesef ulaşamadım. Örneğin, "What is K means, can you explain it to me?" gibi bir sorgu yönelttiğimde, kaynak dokümanda K means'i Türkçe açıklayan yerleri sistem buluyor, ama döngüyü İngilizce vermek yerine Türkçe veriyor. Bu durum ile uğraşmama rağmen net bir çözüme ulaşamadım.

---

# Nerede takıldınız? Nasıl çözdünüz?

İlk tercih ettiğim Gemma modeli ile genel mesajlara güzel cevaplar alamadım. "Nasılsın?" sorgusunda bile "Merhaba" şeklinde basit dönüşler ile karşılığı olmayan cevaplar aldım. Bu durum daha fazla parametre ile eğitilmiş bir model tercih edilerek çözülmüş oldu.

Başlangıçta ChromaDB'nin döndürdüğü skorların düşük olduğunu düşündüm. Belgeler ile sorguda uyum olsa da istediğim dönüşleri alamıyordum. Daha sonra, ChromaDB'nin cosine similarity değil Euclidean distance ölçtüğünü fark ettim. ChromaDB'yi cosine metriği ile yapılandırdım. Bu durumda artık ChromaDB sorgu sonucunda cosine similarity yerine cosine distance döndürdüğü için sonuçları `1 - distance` formülüyle cosine similarity değerine çevirdim. Embedding'ler de normalize edildiği için cosine metriği ile uyumlu şekilde çalıştı. Burada ilginç bir nokta fark ettim; Sentence Transformer modellerinin çoğunlukla pozitif benzerlik skorları üretmesi durumuydu. Proje kapsamında herhangi bir probleme sebebiyet vermedi ama benim ilk etaptaki beklentim -1 ile 1 arasında similarity değerlerini gözlemlemek iken, genellikle 0 ile 1 arasında gözlemledim.

---

# Zamanınızı nasıl harcadınız?

Her modülde aşağıdaki sırayı takip etmeye çalıştım.

1. Önce problemi anlama ve teorik araştırma
2. Alternatiflerin değerlendirilmesi
3. Uygulama
4. Küçük ölçekli manuel testler

Yaklaşık zaman dağılımım şu şekilde oldu.

| Çalışma Alanı                                                      | Oran |
| ------------------------------------------------------------------ | ---: |
| Mimari tasarım ve teknoloji seçimi                                 |  %10 |
| PDF / OCR / Text Processing / Text Cleaning                        |  %15 |
| Chunking, Embedding ve Vector Database                             |  %25 |
| Retrieval ve LLM entegrasyonu                                      |  %25 |
| Prompt Engineering ve Hallucination kontrolü                       |  %10 |
| UI, Logging ve son düzenlemeler                                    |   %5 |
| Testing (Smoke, Integration, Manuel, End-to-End senaryo testleri) |  %10 |


---

# Şu an bildiğinizle baştan başlasanız neyi farklı yapardınız?

• Intention'a karar veren LLM'i daha cok Orchestrator haline getirmek . Bu hem gelen mesaji uygun sekilde dagitacak, ayni suanda yaptigimiz gibi dokuman ile alakali ise RAG’a yonlendirecek, genel mesaj ise genel prompt’a yonlendirecek, ama ayni zamanda uretilen mesajlar final response olarak verilmeden once kontrol edecek. Projenin olceklenmesi durumunda bu orchestrator LLM, gerekirse toollar cagirabilecek.

• Proje kucuk oldugu icin daha hizli calismasi adına extracted textler direkt olarak Llama 3.1 8B’ye prompt olarak verilebilirdi, cunku kullandigimiz bu LLM’in Context Window’u 128K, bu MVP icin yeteri kadar buyuk. Ama bu yaklasimi tercih etseydim, olceklenebilir olmazdi, sadece bu proje bazinda daha hizli islem yapilabilmesi icin deneyebilirdim. 

• Bir öncekine muadil bir başka yaklaşım olarak, best practice icin her zaman Context Window check etmeyi tercih ederdim, ve yuklenilen dokumanlarin buyukluklerini de hesaba katabilirdim. Cunku şöyle bir durum olabilir, salt bir yaklasim olarak eger elimdeki dokumanlarin buyuklugu Context Windowdan kucuk ise, direkt LLM’e hepsini vermek, buyuk ise RAG’a yonlendirmek aslinda net bir cozum yine de olmuyor. Dokumanlarin sayfa sayisi arttikca, LLMin, bunlarin hepsinin icinden gerekli yeri bulmasi yerine, RAG ile vector search yaparak top-k chunk bulmak daha hizli olabilir.

• Ocr yerine image-to-text uzerine egitilmis bir VLM kullanirdim. Daha iyi sonuc verme durumu olabilir diye düşünüyorum. Extracted Text’leri iki sekilde degerlendirmeyi dusunurdum. Bu konu altındakı ikinci ve üçüncü maddelerdeki durumları göz önünde bulundurarak ya DB’ye kaydederdim ya da RAG’a gitmeden JSON olarak tutup response uretecek LLM’e her zaman verirdim. Cunku image’lerdeki textlerin cok yer kaplamasini ilk bakista beklemezdim. Ama olceklenebilirlik icin üçüncü maddedeki gibi her zaman LLM’e direkt vermek yerine Vector DB’ye kaydetme yolunu tercih ederdim.

• PDF icerisinde fotograf olan senaryolari duzeltmek icin bir yontem arastirirdim.