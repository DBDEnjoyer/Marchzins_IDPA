import json, os
import tkinter as tk
from tkinter import messagebox

CFG_FILE = "settings.json"


def load_cfg():
    if os.path.exists(CFG_FILE):
        try:
            return json.load(open(CFG_FILE, "r", encoding="utf-8"))
        except:
            pass
    return {"language":"DE", "default_tax":35.0}

def save_cfg(cfg):
    json.dump(cfg, open(CFG_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

cfg = load_cfg()

def berechne_marchzins(kapital: float, zinssatz: float, geburtstag: str) -> float:
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
    return float(val.replace(",", ".").strip())

def valide_eingaben(kapital, zinssatz, geburtstag, steuersatz):
    try:
        kapital = _to_float(kapital)
        zinssatz = _to_float(zinssatz)
        steuersatz = _to_float(steuersatz)

        if kapital < 0: raise ValueError("Kapital darf nicht negativ sein")
        if zinssatz < 0: raise ValueError("Zinssatz darf nicht negativ sein")
        if not (0 <= steuersatz <= 100): raise ValueError("Steuersatz muss zwischen 0 und 100 liegen")

        parts = geburtstag.split(".")
        if len(parts) != 2: raise ValueError("Geburtstag muss das Format TT.MM haben")
        tag, monat = map(int, parts)
        if not (1 <= tag <= 31 and 1 <= monat <= 12):
            raise ValueError("Ungültiges Datum")

        return kapital, zinssatz, f"{tag:02d}.{monat:02d}", steuersatz, None
    except ValueError as e:
        return None, None, None, None, f"Fehlerhafte Eingabe: {e}"

texts = {
    "DE": {
        "capital": "Kapital (CHF):",
        "rate": "Zinssatz (%):",
        "birthday": "Geburtstag (TT.MM):",
        "tax": "Steuersatz (%):",
        "brutto": "Bruttozins",
        "steuer": "Steuerabzug",
        "netto": "Nettozins",
        "calc": "Berechnen",
        "quit": "Beenden",
        "error": "Fehlerhafte Eingabe"
    },
    "EN": {
        "capital": "Capital (CHF):",
        "rate": "Interest rate (%):",
        "birthday": "Birthday (DD.MM):",
        "tax": "Tax rate (%):",
        "brutto": "Gross interest",
        "steuer": "Tax deduction",
        "netto": "Net interest",
        "calc": "Calculate",
        "quit": "Close",
        "error": "Invalid input"
    }
}

def run_gui(language="DE"):
    lang = texts[language]

    root = tk.Tk()
    root.title("Marchzins-Rechner")

    # Labels & Eingaben
    tk.Label(root, text=lang["capital"]).grid(row=0, column=0, sticky="e")
    entry_kapital = tk.Entry(root); entry_kapital.grid(row=0, column=1)

    tk.Label(root, text=lang["rate"]).grid(row=1, column=0, sticky="e")
    entry_zinssatz = tk.Entry(root); entry_zinssatz.grid(row=1, column=1)

    tk.Label(root, text=lang["birthday"]).grid(row=2, column=0, sticky="e")
    entry_geburtstag = tk.Entry(root); entry_geburtstag.grid(row=2, column=1)

    tk.Label(root, text=lang["tax"]).grid(row=3, column=0, sticky="e")
    entry_steuer = tk.Entry(root)
    entry_steuer.insert(0, str(cfg["default_tax"]))  # Voreinstellung
    entry_steuer.grid(row=3, column=1)

    # Ausgaben
    label_brutto = tk.Label(root, text=f"{lang['brutto']}: -")
    label_brutto.grid(row=5, column=0, columnspan=2)
    label_steuer = tk.Label(root, text=f"{lang['steuer']}: -")
    label_steuer.grid(row=6, column=0, columnspan=2)
    label_netto = tk.Label(root, text=f"{lang['netto']}: -")
    label_netto.grid(row=7, column=0, columnspan=2)

    def berechnen():
        kapital, zinssatz, geburtstag, steuersatz, fehler = valide_eingaben(
            entry_kapital.get(), entry_zinssatz.get(), entry_geburtstag.get(), entry_steuer.get()
        )
        if fehler:
            messagebox.showerror(lang["error"], fehler)
            return
        result = berechne_ausgabe(kapital, zinssatz, geburtstag, steuersatz)
        label_brutto.config(text=f"{lang['brutto']}: {result['Bruttozins']:.2f} CHF")
        label_steuer.config(text=f"{lang['steuer']}: {result['Steuerabzug']:.2f} CHF")
        label_netto.config(text=f"{lang['netto']}: {result['Nettozins']:.2f} CHF")
        # Standard-Steuersatz speichern
        cfg["default_tax"] = steuersatz
        save_cfg(cfg)

    tk.Button(root, text=lang["calc"], command=berechnen).grid(row=4, column=0, columnspan=2)
    tk.Button(root, text=lang["quit"], command=root.destroy).grid(row=8, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    # Sprache aus gespeicherter Config
    run_gui(cfg.get("language","DE"))
