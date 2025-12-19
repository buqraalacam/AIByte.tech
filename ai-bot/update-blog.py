import json
import datetime

# Simüle edilmiş AI ile oluşturulan blog yazısı
new_post = {
    "baslik": "Yapay Zeka ile Otomatik İçerik Üretimi",
    "tarih": datetime.date.today().isoformat(),
    "ozet": "AI artık sadece içerik yazmakla kalmıyor, tüm yayıncılık süreçlerini dönüştürüyor.",
    "link": "#"
}

# Mevcut blog dosyasını yükle
with open('../veriler/bloglar.json', 'r', encoding='utf-8') as f:
    bloglar = json.load(f)

# Yeni yazıyı en üste ekle
bloglar.insert(0, new_post)

# Tekrar yaz
with open('../veriler/bloglar.json', 'w', encoding='utf-8') as f:
    json.dump(bloglar, f, ensure_ascii=False, indent=2)

print("✅ Blog başarıyla güncellendi!")