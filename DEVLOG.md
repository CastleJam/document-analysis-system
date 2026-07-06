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