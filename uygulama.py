"""Sosyolojik görüşme alıntılarını güvenli biçimde temalara göre kaydeder."""

import csv
import os
import re
import unicodedata


def theme_key(theme):
    """Türkçe I/İ harflerini dikkate alarak karşılaştırma anahtarı üretir."""
    normalized = unicodedata.normalize("NFC", theme.strip())
    # DUZELTME: Python casefold, Türkçe İ harfini birleşik i+nokta yapabiliyor.
    # Türkçe tema adlarında I/İ dönüşümünü karşılaştırmadan önce açıkça ele al.
    normalized = normalized.translate(str.maketrans({"I": "ı", "İ": "i"}))
    return unicodedata.normalize("NFC", normalized.casefold())


def normalize_themes(raw_themes):
    """Boşlukları temizler ve aynı temayı bir alıntıda bir kez tutar."""
    themes = []
    seen = set()

    for raw_theme in raw_themes:
        theme = raw_theme.strip()
        key = theme_key(theme)
        if theme and key not in seen:
            themes.append(theme)
            seen.add(key)

    return themes


def add_record(
    records,
    theme_counts,
    theme_names,
    participant_code,
    excerpt,
    raw_themes,
    has_identifiers=False,
    sanitized_excerpt="",
):
    """Girdileri doğrular, gizlilik kontrolünü uygular ve kaydı ekler."""
    participant_code = participant_code.strip()
    excerpt = excerpt.strip()

    if not participant_code:
        return False, "Takma kod boş olamaz."
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,20}", participant_code):
        return False, "Takma kod yalnızca harf, sayı, tire ve alt çizgi içerebilir."
    if not excerpt:
        return False, "Alıntı boş olamaz."

    themes = normalize_themes(raw_themes)
    if not themes:
        return False, "En az bir tema yazmalısınız."

    if has_identifiers:
        safe_excerpt = sanitized_excerpt.strip()
        if not safe_excerpt or safe_excerpt == excerpt:
            return False, "Tanıtıcı ayrıntıları maskeleyip alıntıyı yeniden girin."
    else:
        safe_excerpt = excerpt

    saved_themes = []
    for theme in themes:
        key = theme_key(theme)
        if key in theme_counts:
            theme_counts[key] += 1
            saved_themes.append(theme_names[key])
        else:
            theme_counts[key] = 1
            theme_names[key] = theme
            saved_themes.append(theme)

    records.append(
        {
            "participant_code": participant_code,
            "excerpt": safe_excerpt,
            "themes": saved_themes,
        }
    )
    return True, "Kayıt eklendi."


def format_summary(records, theme_counts, theme_names):
    """Kayıt ve tema toplamlarını okunaklı biçimde hazırlar."""
    lines = ["Kayıt özeti", f"Bu oturumda eklenen kayıt: {len(records)}"]
    if not theme_counts:
        lines.append("Henüz geçerli kayıt yok.")
    else:
        lines.append("Tema sayıları:")
        for key, count in theme_counts.items():
            lines.append(f"- {theme_names[key]}: {count}")
    return "\n".join(lines)


def save_csv(path, records, theme_counts, theme_names):
    """Kayıtları ve tema toplamlarını CSV dosyasına ekler."""
    file_has_content = os.path.exists(path) and os.path.getsize(path) > 0
    with open(path, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        if not file_has_content:
            writer.writerow(
                ["Tür", "Takma kod", "Alıntı", "Temalar", "Tema", "Sayı"]
            )
        for record in records:
            writer.writerow(
                [
                    "Kayıt",
                    record["participant_code"],
                    record["excerpt"],
                    "; ".join(record["themes"]),
                    "",
                    "",
                ]
            )
        for key, count in theme_counts.items():
            writer.writerow(["Tema toplamı", "", "", "", theme_names[key], count])


def ask_yes_no(message):
    """Kullanıcıdan evet/hayır yanıtını tekrar sorarak alır."""
    while True:
        answer = input(message).strip().casefold()
        if answer in ("e", "evet"):
            return True
        if answer in ("h", "hayır", "hayir"):
            return False
        print("Lütfen E (evet) veya H (hayır) yazın.")


def main():
    print("Nitel Görüşme Kodlama Defteri")
    print("Gerçek ad yerine takma kod kullanın; alıntıları kaydetmeden önce gözden geçirin.\n")

    records = []
    theme_counts = {}
    theme_names = {}

    while True:
        participant_code = input("Katılımcı takma kodu: ")
        excerpt = input("Görüşme alıntısı: ")
        raw_themes = input("Tema veya temalar (virgülle ayırın): ").split(",")
        has_identifiers = ask_yes_no("Alıntıda tanıtıcı bilgi var mı? (E/H): ")
        sanitized_excerpt = ""
        if has_identifiers:
            print("Tanıtıcı ayrıntıları [KİŞİ], [YER] gibi ifadelerle maskeleyin.")
            sanitized_excerpt = input("Maskelenmiş alıntıyı girin: ")

        success, message = add_record(
            records,
            theme_counts,
            theme_names,
            participant_code,
            excerpt,
            raw_themes,
            has_identifiers,
            sanitized_excerpt,
        )
        print(message)

        if not ask_yes_no("Yeni kayıt eklemek ister misiniz? (E/H): "):
            break

    print()
    print(format_summary(records, theme_counts, theme_names))
    try:
        save_csv("kodlama_kayitlari.csv", records, theme_counts, theme_names)
        print("Kayıtlar kodlama_kayitlari.csv dosyasına eklendi.")
    except OSError as error:
        print(f"Dosya kaydedilemedi: {error}")


if __name__ == "__main__":
    main()
