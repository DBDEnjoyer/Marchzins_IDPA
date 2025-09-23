# Projekt-Dokumentation

**Bytyqi, Grigioni, Lai**

| Datum      | Version | Zusammenfassung |
| ---------- | ------- | ---------------- |
| 19.08.2025 | 0.0.1   | User Stories erstellt |
| 19.08.2025 | 0.0.2   | Testfälle definiert |
| 26.08.2025 | 0.1.0   | GUI-Skizze entworfen |
| 26.08.2025 | 0.1.1   | Marchzins-Berechnung programmiert |
| 26.08.2025 | 0.1.2   | Brutto-/Netto-Ausgabe mit Steuerabzug ergänzt |
| 15.09.2025 | 0.1.3   | Validierung der Eingaben umgesetzt |
| 15.09.2025 | 0.1.4   | Mehrfach-Berechnungen in einer Session ermöglicht |
| 15.09.2025 | 0.1.5   | Sprachumschaltung (DE/EN) implementiert |
| 22.09.2025 | 0.9.0   | Speicherung von Standardwerten und letzte Tests |
| 24.09.2025 | 1.0.0   | Projekt abgeschlossen und dokumentiert |

---

## 1 Informieren

### 1.1 Ihr Projekt

Wir entwickeln einen **Marchzins-Rechner**, der Brutto-, Steuer- und Nettozins berechnet. Das Programm bietet Eingabevalidierung, Mehrfach-Berechnungen, Sprachumschaltung (DE/EN) und eine einfache GUI für eine übersichtliche Bedienung.

### 1.2 User Stories

| US-№ | Verbindlichkeit | Typ         | Beschreibung |
| ---- | --------------- | ----------- | ------------ |
| 1    | Muss            | Funktional  | Als Nutzer möchte ich eine klare Anleitung sehen, damit ich weiß, wie das Programm funktioniert. |
| 2    | Muss            | Funktional  | Als Nutzer möchte ich den Marchzins berechnen, damit ich meine Zinserträge sehe. |
| 3    | Muss            | Qualität    | Als Nutzer möchte ich, dass Eingaben überprüft werden, damit keine falschen Werte akzeptiert werden. |
| 4    | Muss            | Funktional  | Als Nutzer möchte ich Brutto-, Steuer- und Nettozins sehen, damit ich den Abzug nachvollziehen kann. |
| 5    | Kann            | Rand        | Als Nutzer möchte ich die Sprache umstellen können (DE/EN), damit das Programm international nutzbar ist. |
| 6    | Kann            | Funktional  | Als Nutzer möchte ich, dass Standardwerte gespeichert werden, damit ich diese nicht immer neu eingeben muss. |

### 1.3 Testfälle

| TC-№ | Ausgangslage | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| 1.1  | Programmstart | Enter | Anleitung wird angezeigt |
| 2.1  | Nutzer gibt Kapital, Zinssatz, Geburtstag, Steuersatz ein | 10000, 1.5, 15.03, 35 | Ausgabe: Bruttozins, Steuer, Nettozins |
| 3.1  | Nutzer gibt ungültige Eingabe | „abc“ oder „32.13“ | Fehlermeldung „Fehlerhafte Eingabe“ |
| 4.1  | Nutzer beendet Berechnung | „n“ bzw. „y“ | Programm beendet sich |
| 5.1  | Spracheinstellung EN | Inputs in Englisch | Ausgabe in Englisch |
| 6.1  | Programm wird erneut geöffnet | – | Letzter Steuersatz ist voreingestellt |

---

## 2 Planen

| AP-№ | Frist      | Zuständig | Beschreibung | geplante Zeit |
| ---- | ---------- | --------- | ------------ | ------------- |
| 1.A  | 19.08.2025 | Team      | Projektauftrag analysieren, User Stories & Testfälle erstellen | 45’ |
| 2.A  | 26.08.2025 | Lai       | GUI-Skizze entwerfen | 90’ |
| 2.B  | 26.08.2025 | Grigioni  | Marchzins-Berechnung implementieren | 90’ |
| 2.C  | 26.08.2025 | Bytyqi    | Brutto-/Netto-Ausgabe mit Steuerabzug ergänzen | 90’ |
| 3.A  | 15.09.2025 | Lai       | Eingabevalidierung (Zahlen/Datum) implementieren | 90’ |
| 3.B  | 15.09.2025 | Grigioni  | Session für Mehrfach-Berechnung umsetzen | 90’ |
| 3.C  | 15.09.2025 | Bytyqi    | Sprachumschaltung DE/EN einbauen | 90’ |
| 4.A  | 22.09.2025 | Team      | Speicherung von Standardwerten (Steuersatz, Sprache) implementieren | 90’ |
| 4.B  | 22.09.2025 | Team      | Letzte Tests durchführen, Doku aktualisieren | 90’ |
| 5.A  | 24.09.2025 | Team      | Projektabschluss und Abgabe | 45’ |

Total: ca. 12 Arbeitspakete ≈ 18 Stunden

---

## 3 Entscheiden

- Wir haben uns für **Python** entschieden, weil es einfach und schnell GUI, Input-Validierung und Berechnungen erlaubt.  
- Die GUI wurde mit **tkinter** umgesetzt, weil es in Python integriert ist.  
- Sprachumschaltung und Standardwert-Speicherung wurden als **Kann-Features** umgesetzt, um die Benutzerfreundlichkeit zu erhöhen.  
- Die Eingabevalidierung wurde so implementiert, dass sowohl Punkt als auch Komma erlaubt sind.  

---

## 4 Realisieren

| AP-№ | Datum      | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ---------- | --------- | ------------- | ----------------- |
| 1.A  | 19.08.2025 | Team      | 45’ | 60’ |
| 2.A  | 26.08.2025 | Lai       | 90’ | 90’ |
| 2.B  | 26.08.2025 | Grigioni  | 90’ | 80’ |
| 2.C  | 26.08.2025 | Bytyqi    | 90’ | 90’ |
| 3.A  | 15.09.2025 | Lai       | 90’ | 100’ |
| 3.B  | 15.09.2025 | Grigioni  | 90’ | 85’ |
| 3.C  | 15.09.2025 | Bytyqi    | 90’ | 90’ |
| 4.A  | 22.09.2025 | Team      | 90’ | 95’ |
| 4.B  | 22.09.2025 | Team      | 90’ | 85’ |
| 5.A  | 24.09.2025 | Team      | 45’ | 45’ |

---

## 5 Kontrollieren

### 5.1 Testprotokoll

| TC-№ | Datum      | Resultat | Tester |
| ---- | ---------- | -------- | ------ |
| 1.1  | 19.08.2025 | OK – Anleitung erscheint beim Start | Team |
| 2.1  | 26.08.2025 | OK – Berechnung liefert korrekten Brutto-/Nettozins | Team |
| 3.1  | 15.09.2025 | OK – Ungültige Eingaben werden abgefangen | Team |
| 4.1  | 15.09.2025 | OK – Session kann beendet werden | Team |
| 5.1  | 15.09.2025 | OK – Sprache lässt sich umstellen | Team |
| 6.1  | 22.09.2025 | OK – Standardwerte werden gespeichert | Team |

**Fazit:** Alle Muss-Anforderungen wurden erfüllt, ebenso die Kann-Anforderungen.

### 5.2 Exploratives Testen

| BR-№ | Ausgangslage | Eingabe | Erwartete Ausgabe | Tatsächliche Ausgabe |
| ---- | ------------ | ------- | ----------------- | -------------------- |
| I    | Kapital-Eingabe | „abc“ | Fehlermeldung | Fehlermeldung |
| II   | Geburtstag | „32.13“ | Fehlermeldung | Fehlermeldung |
| III  | Steuer | „150“ | Fehlermeldung | Fehlermeldung |
| IV   | Mehrfach-Berechnung | Neue Werte | Neue Resultate | Neue Resultate |
| V    | Sprache EN | 10000, 1.5, 15.03, 35 | „Gross interest, Tax deduction, Net interest“ | Genau so |

---

## 6 Auswerten

Wir haben gelernt, ein Programm strukturiert zu planen, zu entwickeln und mit Testfällen zu überprüfen. Besonders wichtig war die **Eingabevalidierung**, um Fehler abzufangen.  
Die Umsetzung einer **GUI** hat gezeigt, wie man Programme benutzerfreundlich gestaltet.  
Durch die **Sprachumschaltung und Speicherung von Standardwerten** wurde die Benutzererfahrung verbessert.  
Die Teamarbeit hat reibungslos funktioniert und das Projekt konnte im vorgesehenen Zeitrahmen erfolgreich abgeschlossen werden.
