# ai-bot/ai_blog_generator.py
import json
import os
import random
from datetime import date
from config import BLOG_TOPICS

# Simüle edilmiş AI ile içerik üretimi
def generate_ai_blog_post(topic):
    summaries = {
        "AI": "Yapay zeka artık sadece metin üretmekle kalmıyor; otomatik gelir sistemleri kurabiliyor.",
        "Raspberry Pi": "Raspberry Pi 5 ile ev otomasyonu artık herkesin reach'inde.",
        "Linux": "Terminal becerilerinizi geliştirerek verimliliğinizi 3 katına çıkarabilirsiniz.",
        "Teknoloji": "2025'te en çok talep gören AI araçları listesi hazır!",
        "Otomasyon": "Günlük rutin işlerinizi AI ile devre dışı bırakın."
    }
    return {
        "baslik": f"{topic} ile Geleceği Şekillendir",
        "tarih": date.today().isoformat(),
        "ozet": summaries.get(topic, "Bu konuda yeni bir rehber hazır!"),
        "link": "#"
    }

def main():
    # Mevcut blogları yükle
    blog_file = "veriler/bloglar.json"
    if not os.path.exists(blog_file):
        print("❌ bloglar.json bulunamadı!")
        return

    with open(blog_file, "r", encoding="utf-8") as f:
        bloglar = json.load(f)

    # Rastgele bir konu seç
    topic = random.choice(BLOG_TOPICS)
    new_post = generate_ai_blog_post(topic)

    # Zaten var mı kontrol et (basit kopya engel)
    if not any(post["baslik"] == new_post["baslik"] for post in bloglar):
        bloglar.insert(0, new_post)  # En üste ekle
        print(f"✅ Yeni blog eklendi: {new_post['baslik']}")

        # Kaydet
        with open(blog_file, "w", encoding="utf-8") as f:
            json.dump(bloglar, f, ensure_ascii=False, indent=2)
    else:
        print("ℹ️ Bu başlık zaten var, atlanıyor.")

if __name__ == "__main__":
    main()