Du sollst eine Anwendung entwickeln, die Kunden- und Versicherungsdaten erwaltet. Die Anwendung soll es ermöglichen, Versicherungsnehmer zu erstellen, ihre Policen zu verwalten und Schadensfälle zu bearbeiten. Dabei sollen verschiedene Funktionen wie das Berechnen von Prämien und die Abwicklung von Schadensfällen implementiert werden. Die Aufgaben bauen aufeinander auf und umfassen sowohl grundlegende als auch fortgeschrittene Python-Konzepte.

---

### **Aufgabenstellung:**

### **Aufgabe 1: Klassenstruktur und Initialisierung**

1. Erstelle eine Klasse `Customer`, die die Grundinformationen eines Kunden enthält:
    - `name` (Name des Kunden, als `str`)
    - `policy_type` (Art der Versicherungspolice, als `str`, z.B. "Privat", "Gewerbe")
    - `annual_fee` (Jahresbeitrag, als `float`)
2. Implementiere einen Konstruktor (`__init__`), der die Attribute initialisiert. Verwende Type Hints.
3. Füge eine Methode `__str__` hinzu, die eine lesbare Darstellung des Kunden zurückgibt.
4. Implementiere Getter- und Setter-Methoden für jedes Attribut unter Verwendung von `@property`. Achte darauf, dass der `annual_fee` nur positive Werte annehmen kann. Bei fehlerhaften Eingaben soll eine entsprechende `ValueError` ausgelöst werden.

### **Aufgabe 2: Berechnung der Versicherungsprämie**

1. Erstelle eine Funktion `calculate_discounted_fee`, die den Jahresbeitrag des Kunden basierend auf bestimmten Bedingungen reduziert:
    - 5% Rabatt für "Privat"-Kunden
    - 10% Rabatt für "Gewerbe"-Kunden
2. Berechne für beide Fälle den rabattierten Jahresbeitrag und gib diesen zurück. Nutze Lambda-Funktionen innerhalb der Methode zur Berechnung des Rabatts.

### **Aufgabe 3: Liste und Verwaltung der Kundendaten**

1. Erstelle eine Liste mit mehreren `Customer`Objekten, die verschiedene Kundentypen und Jahresbeiträge repräsentieren.
2. Verwende eine **List Comprehension**, um eine neue Liste zu erstellen, die nur Kunden mit einer Jahresprämie von mehr als 300 Euro enthält.
3. Nutze `sorted()` mit einer **Lambda-Funktion** als Schlüssel, um die Kundenliste basierend auf ihrem Jahresbeitrag aufsteigend zu sortieren.

### **Aufgabe 4: Erweiterung um Policenverwaltung und Zusatzoptionen**

1. Erstelle eine Klasse `InsurancePolicy`, die grundlegende Informationen zur Rechtsschutzversicherungspolice enthält:
    - `policy_id` (Policen-ID, `int`)
    - `coverage_amount` (Deckungssumme, `float`)
    - `additional_options` (Liste von Optionen wie ["Arbeitsrechtsschutz", "Verkehrsrechtsschutz"])
2. Implementiere eine Methode `add_option`, die eine zusätzliche Versicherungsoption zur Liste hinzufügt, falls diese noch nicht vorhanden ist.
3. Verwende eine **List Comprehension**, um mehrere neue Optionen zur Liste hinzuzufügen.

### **Aufgabe 5: Beziehungen zwischen Kunden und Versicherungen**

1. Erstelle eine Klasse `CustomerPolicyManagement`, die die Beziehung zwischen Kunden und Policen verwaltet. Diese Klasse sollte ein **Dictionary** enthalten, in dem jeder Kunde als Schlüssel und die entsprechende `InsurancePolicy` als Wert gespeichert wird.
2. Implementiere eine Methode `assign_policy_to_customer`, die einer Kundeninstanz eine Police zuordnet. Nutze hierbei **Exceptions** zur Fehlerbehandlung, falls ein Kunde bereits eine zugewiesene Police hat.
3. Füge eine Methode hinzu, um alle Kunden mit einer bestimmten Deckungssumme zu finden. Verwende hierzu eine **Lambda-Funktion** und `filter()`.

### **Aufgabe 6: Schadensfallverwaltung**

1. Erstelle eine Klasse `Claim`, die folgende Attribute enthält:
    - `description`: Beschreibung des Schadensfalls (String)
    - `amount`: Der Betrag des Schadens (float)
    - `processed`: Ein boolescher Wert, der angibt, ob der Fall bearbeitet wurde oder nicht
2. Implementiere Methoden:
    - **`process_claim(self)`**: Setzt den Status des Schadensfalls auf "bearbeitet".
    - **`is_valid_claim(self)`**: Prüft, ob der Schadensbetrag innerhalb der Deckungssumme liegt.
3. Implementiere Fehlerbehandlung in der Methode `process_claim()`, sodass bei einem Schadensbetrag über der Deckungssumme eine benutzerdefinierte Exception (`CoverageExceededError`) geworfen wird.

### **Aufgabe 7: Erweiterung um VIP-Kunden**

1. Erstelle eine Unterklasse `VIPCustomer`, die von der Klasse `Customer` erbt:
    - VIP-Kunden erhalten einen zusätzlichen Rabatt von 15% auf ihre Prämien.
    - Implementiere in dieser Klasse eine Methode zur Berechnung der rabattierten Prämie unter Berücksichtigung des VIP-Rabatts.
2. Erweitere das System so, dass VIP-Kunden spezielle Zusatzoptionen wie „VIP-Rechtsschutz“ erhalten können.

### **Aufgabe 8: CSV-Import/Export**

1. Implementiere Funktionen zum Importieren und Exportieren von Kundendaten aus einer CSV-Datei:
    - Die CSV-Datei enthält Spalten für Name, Policentyp und Jahresprämie.
    - Schreibe Funktionen zum Einlesen der Daten in Customer-Objekte sowie zum Exportieren bestehender Kundendaten in eine CSV-Datei.

## **Bonus-Aufgaben (optional):**

### **Aufgabe 9: Erweiterte Berichts- und Statistikfunktionen**

1. Füge eine Methode hinzu, die einen Bericht über alle Kunden erstellt:
    - Der Bericht soll den Namen des Kunden sowie den Gesamtbetrag aller Prämien enthalten.
    - Nutze hierfür f-Strings sowie List Comprehensions für die Formatierung.
2. Implementiere statistische Auswertungen über alle Policen:
    - Durchschnittliche Deckungssumme aller Policen
    - Anzahl bearbeiteter vs unbearbeiteter Schadensfälle

---

### Lernziele:

- Ihre Kenntnisse in OOP vertiefen und lernen Klassenstrukturen effizient aufzubauen.
- Den Einsatz von Lambda-Funktionen und List Comprehensions üben.
- Fehlerbehandlung durch benutzerdefinierte Exceptions anwenden.
- Datenstrukturen wie Listen und Dictionaries zur Verwaltung von Objekten nutzen.
- Praktische Anwendungen im Bereich Rechtsschutzversicherung entwickeln.

---

## **Bonus-Aufgabe: Statistische Analyse und Visualisierung**

In dieser Bonus-Aufgabe sollen Sie numpy, pandas und matplotlib verwenden, um eine weiterführende Analyse und Visualisierung von Kunden- und Schadensfalldaten durchzuführen. Ziel ist es, grundlegende statistische Auswertungen durchzuführen und die Daten anschaulich darzustellen.

---

### **Teil 1: Statistische Auswertung mit numpy und pandas**

1. **Erstellen Sie eine pandas DataFrame** mit Kundendaten, der folgende Spalten enthält:
    - `name`: Name des Kunden
    - `policy_type`: Art der Versicherungspolice (z.B. "Privat", "Gewerbe")
    - `annual_fee`: Jahresbeitrag
    - `is_vip`: Gibt an, ob der Kunde ein VIP-Kunde ist (Boolean)
2. **Berechnen Sie statistische Kennzahlen**:
    - Durchschnittlicher Jahresbeitrag für alle Kunden.
    - Durchschnittlicher Jahresbeitrag, getrennt nach Policentyp (z.B. "Privat" und "Gewerbe").
    - Standardabweichung des Jahresbeitrags (Gesamtdurchschnitt).
3. **Untersuchen Sie Schadensfalldaten**:
    - Laden Sie alle Schadensfälle in einen DataFrame mit den Spalten `customer_name`, `description`, `amount`, `processed`.
    - Berechnen Sie die Gesamtsumme aller Schadensbeträge.
    - Ermitteln Sie den durchschnittlichen Schadenswert für bearbeitete und unbearbeitete Fälle.

---

### **Teil 2: Datenvisualisierung mit matplotlib**

1. **Visualisieren Sie die Jahresbeiträge**:
    - Erstellen Sie ein Balkendiagramm, das die durchschnittlichen Jahresbeiträge für „Privat“- und „Gewerbe“-Kunden vergleicht.
2. **Erstellen Sie ein Kreisdiagramm**:
    - Zeigen Sie die Verteilung bearbeiteter und unbearbeiteter Schadensfälle an, um eine schnelle Übersicht zu geben.
3. **Histogramm der Schadensbeträge**:
    - Visualisieren Sie die Verteilung der Schadensbeträge als Histogramm. Nutzen Sie numpy, um die Schadensbeträge in sinnvolle Intervalle zu unterteilen und eine Übersicht über häufige Schadensgrößen zu geben.

---

### **Erwartete Ergebnisse und Lernziele**

- Sie sollen grundlegende Fähigkeiten in der Datenmanipulation und -analyse mit pandas entwickeln.
- Die Nutzung von numpy zur statistischen Analyse und zur Gruppierung und Teilung von Daten erlernen.
- Eine Einführung in matplotlib erhalten und grundlegende Diagramme erstellen, um Daten visuell aufzubereiten.