# Aktivitäten-Planer

Ein einfaches Konsolen-Programm, das mithilfe von Google Gemini AI personalisierte Ausflugstipps für verschiedene Städte generiert.

## Funktionen

- **Stadtauswahl**: Gib eine beliebige Stadt ein.
- **Vibe-Modus**: Wähle zwischen "Action" und "Entspannung".
- **AI-Integration**: Erhält Echtzeit-Vorschläge von Google Gemini.
- **MVC-Architektur**: Saubere Trennung von Daten (Model), Logik (Controller) und Anzeige (View).

## Architektur

Das Projekt folgt dem Model-View-Controller (MVC) Muster:

![MVC Architektur](https://mermaid.ink/img/Z3JhcGggVEQNCiAgICBNYWluKFtNYWluXSkNCiAgICBVc2VyKChCZW51dHplcikpDQogICAgDQogICAgc3ViZ3JhcGggVmlldw0KICAgICAgQ1ZbQ29uc29sZVZpZXddDQogICAgZW5kDQogICAgDQogICAgc3ViZ3JhcGggQ29udHJvbGxlcg0KICAgICAgQUNbQXBwQ29udHJvbGxlcl0NCiAgICBlbmQNCiAgICANCiAgICBzdWJncmFwaCBNb2RlbA0KICAgICAgVERbVHJpcERhdGFdDQogICAgICBHU1tHZW1pbmlTZXJ2aWNlXQ0KICAgIGVuZA0KDQogICAgTWFpbiAtLT58U3RhcnRldHwgQUMNCiAgICBBQyAtLT58UnVmdCBhdWZ8IENWDQogICAgQ1YgPC0tPnxJbnRlcmFrdGlvbnwgVXNlcg0KICAgIENWIC0tPnxHaWJ0IEVpbmdhYmVuIHp1csO8Y2t8IEFDDQogICAgQUMgLS0+fFNwZWljaGVydCBadXN0YW5kfCBURA0KICAgIEFDIC0tPnxGcmFndCBUaXBwcyBhYnwgR1MNCiAgICBHUyAtLT58TGllZmVydCBUaXBwc3wgQUMNCiAgICBBQyAtLT58WmVpZ3QgRXJnZWJuaXNzZXwgQ1YNCg==)

## Programmablauf

Der Ablauf der Anwendung gliedert sich in folgende Schritte:

**<u>1. Initialisierung</u>**
Das Programm startet über die `main.py`. Der **AppController** wird erstellt, welcher wiederum das **Daten-Model** (für Stadt, Personen, Vibe) und die **ConsoleView** (für die Anzeige) initialisiert.

**<u>2. Benutzereingaben</u>**
Der Controller steuert die Abfrage der Informationen über den View:
1. **Ort**: Wohin soll die Reise gehen?
2. **Gruppengröße**: Wie viele Personen sind dabei?
3. **Vibe**: Soll es eher actionreich oder entspannt sein?

**<u>3. Verarbeitung & AI-Anfrage</u>**
Sobald alle Daten vorliegen, sendet der Controller eine Anfrage an den **GeminiService**. Dieser generiert über die Google AI passende Reisetipps, die spezifisch auf den Ort, die Gruppengröße und die gewählte Stimmung zugeschnitten sind.

**<u>4. Ausgabe</u>**
Die empfangenen Tipps werden im Model gespeichert und anschließend über den View übersichtlich in der Konsole ausgegeben. Danach beginnt der Prozess von vorne, bis der Nutzer "Ende" eingibt.

## Voraussetzungen

- Python 3.8 oder höher
- Ein Google Cloud API Key für Gemini (generative AI)

## Installation

1. Repository klonen oder herunterladen.
2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```
3. `.env` Datei erstellen:
   Erstelle eine Datei namens `.env` im Hauptverzeichnis und füge deinen API-Key hinzu:
   ```env
   GEMINI_API_KEY=Dein_API_Key_Hier
   ```

## Starten

Führe das Programm über die `main.py` aus:

```bash
python main.py
```

## Projektstruktur

- `app/controller`: Steuert den Programmablauf.
- `app/model`: Verwaltet Daten und die AI-Kommunikation.
- `app/view`: Kümmert sich um Ein- und Ausgaben in der Konsole.
- `main.py`: Startpunkt der Anwendung.
