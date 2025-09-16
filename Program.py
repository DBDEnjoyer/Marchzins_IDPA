def berechne_marchzins(kapital: float, zinssatz: float, geburtstag: str) -> float:
    # Tage: vom 1. bis inkl. Geburtstag (Bankjahr 360)
    tag, monat = map(int, geburtstag.split("."))
    tage = tag
    zins = (kapital * zinssatz * tage) / (360 * 100)
    return round(zins, 2)

def berechne_ausgabe(kapital: float, zinssatz: float, geburtstag: str, steuersatz: float) -> dict:
    brutto = berechne_marchzins(kapital, zinssatz, geburtstag)
    steuer = round(brutto * steuersatz / 100, 2)
    netto = round(brutto - steuer, 2)
    return {"Bruttozins": brutto, "Steuerabzug": steuer, "Nettozins": netto}

def _to_float(val: str) -> float:
    # erlaubt 1,5 und 1.5
    return float(val.replace(",", ".").strip())

def valide_eingaben(kapital, zinssatz, geburtstag, steuersatz):
    try:
        kapital = _to_float(kapital)
        zinssatz = _to_float(zinssatz)
        steuersatz = _to_float(steuersatz)

        # Basis-Prüfungen
        if kapital < 0: raise ValueError("Kapital darf nicht negativ sein")
        if zinssatz < 0: raise ValueError("Zinssatz darf nicht negativ sein")
        if not (0 <= steuersatz <= 100): raise ValueError("Steuersatz muss zwischen 0 und 100 liegen")

        # Geburtstag prüfen (Format TT.MM, Tag 1..31, Monat 1..12). Monat wird nicht verwendet, ist aber formal korrekt.
        parts = geburtstag.split(".")
        if len(parts) != 2 or any(p.strip() == "" for p in parts):
            raise ValueError("Geburtstag muss das Format TT.MM haben")
        tag, monat = map(int, parts)
        if not (1 <= tag <= 31 and 1 <= monat <= 12):
            raise ValueError("Geburtstag außerhalb gültiger Werte (TT 1–31, MM 1–12)")

        return kapital, zinssatz, f"{tag:02d}.{monat:02d}", steuersatz, None
    except ValueError as e:
        return None, None, None, None, f"Fehlerhafte Eingabe: {e}"

texts = {
    "DE": {
        "capital": "Kapital (CHF): ",
        "rate": "Zinssatz (%): ",
        "birthday": "Geburtstag (TT.MM): ",
        "tax": "Steuersatz (%): ",
        "brutto": "Bruttozins",
        "steuer": "Steuerabzug",
        "netto": "Nettozins",
        "again": "Noch eine Berechnung? (j/n): ",
        "end": "Programm beendet."
    },
    "EN": {
        "capital": "Capital (CHF): ",
        "rate": "Interest rate (%): ",
        "birthday": "Birthday (DD.MM): ",
        "tax": "Tax rate (%): ",
        "brutto": "Gross interest",
        "steuer": "Tax deduction",
        "netto": "Net interest",
        "again": "Another calculation? (y/n): ",
        "end": "Program closed."
    }
}

def start_session(language="DE"):
    lang = texts[language]
    while True:
        kapital = input(lang["capital"])
        zinssatz = input(lang["rate"])
        geburtstag = input(lang["birthday"])
        steuersatz = input(lang["tax"])

        kapital, zinssatz, geburtstag, steuersatz, fehler = valide_eingaben(kapital, zinssatz, geburtstag, steuersatz)
        if fehler:
            print(fehler)
            continue

        ergebnis = berechne_ausgabe(kapital, zinssatz, geburtstag, steuersatz)
        print(f"{lang['brutto']}: {ergebnis['Bruttozins']} CHF")
        print(f"{lang['steuer']}: {ergebnis['Steuerabzug']} CHF")
        print(f"{lang['netto']}: {ergebnis['Nettozins']} CHF")

        nochmal = input(lang["again"]).lower().strip()
        if (language == "DE" and nochmal != "j") or (language == "EN" and nochmal != "y"):
            print(lang["end"])
            break
