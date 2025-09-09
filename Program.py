from datetime import datetime

def berechne_marchzins(kapital: float, zinssatz: float, geburtstag: str) -> float:
    """
    Berechnet den Marchzins-Bonus.
    
    :param kapital: Sparkapital in CHF
    :param zinssatz: Zinssatz in Prozent (z.B. 1.5)
    :param geburtstag: Geburtstag im Format 'TT.MM'
    :return: Marchzins-Bonus in CHF
    """
    tag, monat = map(int, geburtstag.split("."))
    
    tage = tag  
    
    
    zins = (kapital * zinssatz * tage) / (360 * 100)
    return round(zins, 2)


print(berechne_marchzins(10000, 1.5, "15.03"))  

def berechne_ausgabe(kapital: float, zinssatz: float, geburtstag: str, steuersatz: float) -> dict:
    """
    Berechnet Brutto-, Steuer- und Nettozins.
    """
    brutto = berechne_marchzins(kapital, zinssatz, geburtstag)
    steuer = round(brutto * steuersatz / 100, 2)
    netto = round(brutto - steuer, 2)
    
    return {
        "Bruttozins": brutto,
        "Steuerabzug": steuer,
        "Nettozins": netto
    }


ergebnis = berechne_ausgabe(10000, 1.5, "15.03", 35)
print(ergebnis)

def valide_eingaben(kapital, zinssatz, geburtstag, steuersatz):
    try:
        kapital = float(kapital)
        zinssatz = float(zinssatz)
        steuersatz = float(steuersatz)

        tag, monat = map(int, geburtstag.split("."))
        if not (1 <= tag <= 31 and 1 <= monat <= 12):
            raise ValueError("Ungültiges Datum")
        return kapital, zinssatz, geburtstag, steuersatz, None
    except ValueError as e:
        return None, None, None, None, f"Fehlerhafte Eingabe: {e}"

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

        nochmal = input(lang["again"]).lower()
        if (language == "DE" and nochmal != "j") or (language == "EN" and nochmal != "y"):
            print(lang["end"])
            break


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


