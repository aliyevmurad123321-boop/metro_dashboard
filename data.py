from datetime import datetime, timezone, timedelta

STANSIYALAR = {
    "Xətt 1": ["İçərişəhər", "Sahil", "28 May", "Gənclik",
               "Nəriman Nərimanov", "Bakmil", "Ulduz", "Qara Qarayev",
               "Neftçilər", "Xalqlar Dostluğu", "Əhmədli", "Həzi Aslanov"],
    "Xətt 2": ["Xətai", "8 Noyabr", "Avtovağzal", "Memar Əcəmi",
               "Nəsimi", "Azadlıq Prospekti", "Dərnəgül", "Cəfər Cabbarlı"],
    "Xətt 3": ["Koroğlu", "Xocəsən"]
}

STANSIЯ_WEIGHT = {
    "28 May": 1.5, "Gənclik": 1.4, "Nəriman Nərimanov": 1.3,
    "Koroğlu": 1.3, "Memar Əcəmi": 1.2, "Nəsimi": 1.2,
    "İçərişəhər": 0.8, "Həzi Aslanov": 0.9, "Xocəsən": 0.7
}

def get_sixliq_data():
    baku_tz = timezone(timedelta(hours=4))
    now = datetime.now(baku_tz)
    saat = now.hour
    gun = now.weekday()

    if saat < 6:
        base = 0
    elif 7 <= saat <= 9:
        base = 85
    elif 17 <= saat <= 19:
        base = 90
    elif 12 <= saat <= 14:
        base = 60
    else:
        base = 35

    if gun >= 5:
        base = int(base * 0.6)

    import random
    data = {}
    for xett, stansiyalar in STANSIYALAR.items():
        for stansiya in stansiyalar:
            weight = STANSIЯ_WEIGHT.get(stansiya, 1.0)
            sixliq = min(100, int(base * weight + random.randint(-10, 10)))
            sixliq = max(0, sixliq)
            data[stansiya] = {
                "sixliq": sixliq,
                "gozleyen": int(sixliq * 2.5),
                "xett": xett
            }
    return data