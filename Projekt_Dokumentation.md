# Projekt-Dokumentation  

**Gruppe:** Bytyqi, Grigioni, Lai  

| Datum      | Version | Zusammenfassung                                                                 |
| ---------- | ------- | ------------------------------------------------------------------------------- |
| 25.08.2025 | 0.0.1   | Projektauftrag gelesen, Anforderungen und Stakeholder-Wünsche analysiert.       |
| 25.08.2025 | 0.1.0   | Erste User Stories formuliert und Testfälle vorbereitet.                        |
| 01.09.2025 | 0.2.0   ||
| 08.09.2025 | 0.5.0   ||
| 15.09.2025 | 0.7.0   ||
| 22.09.2025 | 0.9.0   ||
| 24.09.2025 | 1.0.0   | Projekt abgeschlossen und Abgegeben|

---

## 1 Informieren  

### 1.1 Ihr Projekt  
Ein benutzerfreundliches Tool zur schnellen und fehlerfreien Berechnung des **Marchzins-Bonus** für Bankkund:innen.  

---

### 1.2 User Stories  

| US-№ | Verbindlichkeit | Typ         | Beschreibung                                                                 |
| ---- | --------------- | ----------- | ----------------------------------------------------------------------------- |
| 1    | Muss            | Funktional  | Als Kundenberater möchte ich den Marchzins einfach berechnen können, damit ich Kunden schnell Auskunft geben kann. |
| 2    | Muss            | Qualität    | Als Bankmitarbeiter möchte ich eine übersichtliche Ausgabe sehen, damit auch neue Mitarbeitende das Tool sofort nutzen können. |
| 3    | Muss            | Funktional  | Als Kundin möchte ich brutto Zinsen, Steuerabzug und Netto-Betrag sehen, damit ich alles nachvollziehen kann. |
| 4    | Muss            | Funktional  | Als System möchte ich falsche Eingaben abfangen, damit keine Fehler entstehen. |
| 5    | Kann            | Funktional  | Als Kundenberater möchte ich mehrere Berechnungen nacheinander durchführen können, ohne das Programm neu starten zu müssen. |
| 6    | Kann            | Funktional  | Als Marketing möchte ich, dass das Tool zweisprachig ist (Deutsch/Englisch), damit auch fremdsprachige Kunden es nutzen können. |
| 7    | Kann            | Qualität| Als IT-Abteilung möchte ich gewisse Voreinstellungen speichern können, ohne sensible Daten abzulegen. |

---

### 1.3 Testfälle  

| TC-№ | Ausgangslage                  | Eingabe                           | Erwartete Ausgabe                                   |
| ---- | ----------------------------- | --------------------------------- | --------------------------------------------------- |
| 1.1  | Tool geöffnet                 | Kapital: 10’000, Zinssatz 1.5 %, Geburtstag: 15.3. | Marchzins korrekt berechnet und angezeigt.          |
| 2.1  | Mitarbeiter startet Programm  | Berechnung durchgeführt            | Klare, gut lesbare Ausgabe im GUI.                  |
| 3.1  | Kunde möchte Details          | Kapital: 5000, Zinssatz 2 %, Steuer 35 % | Bruttozins, Steuerbetrag, Nettozins werden angezeigt. |
| 4.1  | Nutzer gibt Text statt Zahl ein | Kapital: „abc“                     | Fehlermeldung „Bitte Zahl eingeben“ erscheint.      |
| 5.1  | Nach erster Berechnung        | Neue Werte eingeben                 | Zweite Berechnung ohne Neustart möglich.            |
| 6.1  | Nutzer stellt Sprache um      | Sprache: Englisch                  | Ausgabe wechselt auf Englisch.                      |
| 7.1  | IT-Abteilung speichert Setting | Standard-Steuersatz: 35 %          | Beim nächsten Start ist Steuersatz vorausgefüllt.   |

---

### 1.4 Diagramme  

- **Use-Case-Diagramm**: zeigt Kundenberater, Kundin und IT-Abteilung als Akteure.  
- **Programmablaufplan (PAP)**: Eingabe → Berechnung → Ausgabe/Fehlerprüfung.  

---

## 2 Planen  

| AP-№ | Frist      | Zuständig  | Beschreibung                                               | geplante Zeit |
| ---- | ---------- | ---------- | ---------------------------------------------------------- | ------------- |
| 1.A  | 01.09.2025 | Artur      | User Stories formulieren                                   | 45’           |
| 1.B  | 01.09.2025 | Leonardo   | Testfälle erstellen                                        | 45’           |
| 1.C  | 05.09.2025 | Syuan-Yu   | GUI-Entwurf skizzieren                                     | 90’           |
| 2.A  | 10.09.2025 | Leonardo   | Berechnungslogik (Formel Marchzins) implementieren         | 90’           |
| 2.B  | 10.09.2025 | Artur      | Brutto-/Netto-Ausgabe + Steuerabzug implementieren         | 90’           |
| 3.A  | 15.09.2025 | Syuan-Yu   | Fehlerbehandlung (Input-Validierung)                       | 90’           |
| 4.A  | 15.09.2025 | Leonardo   | Mehrfach-Berechnung (Session) implementieren               | 90’           |
| 5.A  | 15.09.2025 | Artur      | Spracheinstellungen (DE/EN) umsetzen                       | 90’           |
| 6.A  | 20.09.2025 | Syuan-Yu   | Settings speichern (Steuersatz)                           | 90’           |
| 7.A  | 20.09.2025 | Team       | Programm gemeinsam testen (alle Testfälle durchgehen)     | 180’          |
| 8.A  | 24.09.2025 | Team       | Dokumentation finalisieren + Präsentation vorbereiten     | 180’          |

**Total:** ca. 16 Arbeitspakete → entspricht 2 Sitzungen × 3 Mitglieder × 4 Arbeitspakete.  
