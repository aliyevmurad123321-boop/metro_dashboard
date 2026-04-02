import random

STANSIYALAR = [
    # Xətt 1 (Qırmızı)
    "İçərişəhər", "Sahil", "28 May", "Gənclik",
    "Nəriman Nərimanov", "Bakmil", "Ulduz", "Qara Qarayev",
    "Neftçilər", "Xalqlar Dostluğu", "Əhmədli", "Həzi Aslanov",
    # Xətt 2 (Yaşıl)
    "Xətai", "8 Noyabr", "Avtovağzal",
    "Memar Əcəmi", "Nəsimi", "Azadlıq Prospekti",
    "Dərnəgül", "Cəfər Cabbarlı",
    # Xətt 3
    "Koroğlu", "Xocəsən"
]

def get_sixliq_data():
    data = {}
    for stansiya in STANSIYALAR:
        data[stansiya] = {
            "sixliq": random.randint(10, 100),
            "gozleyen": random.randint(5, 300)
        }
    return data