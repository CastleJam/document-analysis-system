# Development Log
- Initial project structure
- FASTAPI and Upload endpoint setup for PDF and image files
- Document Processor
    - Document processor service setup
    - Uploaded file type detection 

- Text Extraction
    - PDF parsing using pdfplumber (pdf_parser_service)
    - OCR support using Tesseract  (ocr_service)
    
    + Image based text extraction give some issue on some documents, providing the text with missing characters, make up characters. 

    
- Text Cleaning
    -Çoklu boş satırları azalt
    -Satır sonu/başı boşluklarını temizle
    Removes lines consisting only of symbols.
    Cleans up repeating lines.
    Normalizes spaces.
    -Kontrol karakterlerini kaldır
    -Sayfa markerlarını koru

    + Cok buyuk boyutlu, veya Index, Table of Content gibi kisimlar iceren PDFlerde sorun cikabilir, optimize edilmesi gerekir.

- Chunking
    - Chunking yontemleri dusunuldu, Character Chunking, Sentence Chunking, Paragraph Chunking, Recursive Chunking, Semantic Chunking.
    - Recursive Chunking sektordeki best practicelerden birisi oldugu ve LangChain tarafinda desteklendigi icin secilmistir. Semantic Chunking guzel sonuc verecektir diye dusundum ama onun icin embedding model gerekecek ve daha fazla islem maliyeti, debugginge sebep olacaktir, ilk MVP icin onu uygun gormedim.
    - İlk MVP için 1000 karakter chunk size ve 200 karakter overlap seçildi. Bu değerler, küçük ve orta boy belgelerde anlam bütünlüğünü korurken retrieval maliyetini düşük tutmak için dengeli bir başlangıç noktası olarak belirlendi. Ileride optimize edilebilir.

- Embedding
    -For the embedding layer, `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` was selected. Following alternatives were evaluated

    - `all-MiniLM-L6-v2` was considered because it is lightweight, fast, and widely used in semantic search tasks. However, it is mainly optimized for English, while the case study requires both Turkish and English document support.

    - `intfloat/multilingual-e5-small` was considered because it is multilingual and retrieval-oriented. However, it requires a query/passage prefix structure, which would add extra implementation complexity for the MVP.

    - `BAAI/bge-m3` was considered as a strong multilingual retrieval model. However, it is heavier than needed for the MVP and may increase setup and runtime requirements.

    - OpenAI Embeddings were also considered because of their strong embedding quality. However, they introduce API dependency, possible cost, and data privacy concerns since document chunks would be sent to an external service.

    - A standard BERT-based embedding approach was not preferred because BERT is not directly optimized for sentence-level semantic search without additional pooling or fine-tuning.

    - Based on these considerations, `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` was selected. It supports Turkish and English, runs locally, is lightweight enough for CPU-based MVP development, produces 384-dimensional embeddings, and integrates easily with ChromaDB.

-Vector Database Seçimi

    -Vector database tercihi için FAISS, ChromaDB ve Pinecone alternatifleri değerlendirildi. Aşağıdaki  değerlendirmeler ışığında bu MVP için ChromaDB seçildi.

    -FAISS, küçük ve orta ölçekli projelerde yüksek performanslı ve hafif bir seçenek olarak değerlendirildi. Ancak metadata yönetimi ve kalıcı veri saklama tarafında ek geliştirme ihtiyacı doğurabileceği için MVP kapsamında ikinci planda bırakıldı.

    -ChromaDB, Python tabanlı olması, RAG projelerinde yaygın kullanılması, local çalışabilmesi, kolay kurulum sunması ve chunk bazlı metadata tutabilmesi nedeniyle tercih edildi. Bu projede her chunk için dosya adı, sayfa numarası, chunk ID, dosya tipi, dil bilgisi ve yükleme zamanı gibi metadata bilgilerini saklamak istiyoruz. Bu nedenle ChromaDB, yalnızca vektör araması yapmakla kalmayıp belge takibi ve kaynak gösterme açısından da daha uygun bir seçenek olarak değerlendirildi.

    -Pinecone ise ölçeklenebilir ve production-ready bir cloud vector database çözümü olarak değerlendirildi. Ancak ücretli olması, API bağımlılığı getirmesi ve belge verilerinin dış bir servise gönderilmesi nedeniyle MVP kapsamında tercih edilmedi. Proje ileride daha büyük veri hacimlerine veya çok kullanıcılı production ortamına taşınırsa Pinecone gibi managed vector database çözümleri yeniden değerlendirilebilir.

    -ChromaDB'yi cosine metriği ile yapılandırdım. ChromaDB sorgu sonucunda cosine similarity yerine cosine distance döndürdüğü için, sonuçları 1 - distance formülüyle tekrar cosine similarity değerine çevirdim. Embedding'ler normalize_embeddings=True ile üretildiğinden cosine metriği ile en uyumlu şekilde çalışmaktadır. Pratikte Sentence Transformer modelleri çoğunlukla pozitif benzerlik skorları ürettiği için similarity değerleri genellikle 0 ile 1 arasında gözlemlenmektedir.

- LLM Entegrasyonu
    Iki farkli yaklasim dusunuldu
    
    Yazilan yazinin general bir yazi olup olmadigini rule based ile mi karar vermek yoksa LLM'e reasoning yaptirtip intent'in general mesaj olduguna LLM'in kendisinin mi karar vermesi

    RAG'a gitme senaryolarinda ChromaDB'den donen chunklarin similaritysine bakip, belirlenen bir thresholda gore cevap verip vermeme, veya LLM'in kendisinin reasoning yapip cevap verip vermemesini kendisine birakmak

    Karsilasilan problemlerden birisi LLM'in Turkce soruya Turkce, Ingilizce soruya Ingilizce cevap verirken kafasinin karismasi, oyleki Korece ifadeler sunmus bile olmasi. Ayrica "Nasilsin?" sorusunda general message oldugunu algilamak yerine RAG'a basvurmasi ve cevap olarak "I could not find it in the documents" gibi bir cevap veriyor olmasi iyi sonuclar vermedigini ve adjustments gerekliligini gosterdi. Bu durumda Google Gemma 1B kucuk bir model olarak yetersiz kalmis olabilir diye degerlendirildi. Muadil olarak reasoning yapabilen llama3.1 8B enntegre edildi. Sonuc olarak gelistirme saglandi ve llama3.1 8B kullanimina karar verildi.

    RAG'a gittigi senaryolarda, retrieve ettigi source'da yazan dil ney ise, soruyu farkli dille sormamiza ragmen kaynak dokumandaki dil ile cevap vermesi karsilasilan problemlerden birisidir.
    