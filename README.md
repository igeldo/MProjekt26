# Aktivitäten-Planer

Ein einfaches Konsolen-Programm, das mithilfe von Google Gemini AI personalisierte Ausflugstipps für verschiedene Städte generiert.

## Funktionen

- **Stadtauswahl**: Gib eine beliebige Stadt ein.
- **Vibe-Modus**: Wähle zwischen "Action" und "Entspannung".
- **AI-Integration**: Erhält Echtzeit-Vorschläge von Google Gemini.
- **MVC-Architektur**: Saubere Trennung von Daten (Model), Logik (Controller) und Anzeige (View).

## Architektur

Das Projekt folgt dem Model-View-Controller (MVC) Muster:

![MVC Architektur](https://mermaid.ink/img/Z3JhcGggVEQNCiAgICBVc2VyKChCZW51dHplcikpDQogICAgDQogICAgc3ViZ3JhcGggVmlldw0KICAgICAgQ1ZbQ29uc29sZVZpZXddDQogICAgZW5kDQogICAgDQogICAgc3ViZ3JhcGggQ29udHJvbGxlcg0KICAgICAgQUNbQXBwQ29udHJvbGxlcl0NCiAgICBlbmQNCiAgICANCiAgICBzdWJncmFwaCBNb2RlbA0KICAgICAgVERbVHJpcERhdGFdDQogICAgICBHU1tHZW1pbmlTZXJ2aWNlXQ0KICAgIGVuZA0KDQogICAgVXNlciAtLT58TGllc3QgJiBUaXBwdHwgQ1YNCiAgICBDViAtLT58R2lidCBFaW5nYWJlIHdlaXRlcnwgQUMNCiAgICBBQyAtLT58U2V0enQgWnVzdGFuZHwgVEQNCiAgICBBQyAtLT58UnVmdCBhYnwgR1MNCiAgICBHUyAtLT58TGllZmVydCBUaXBwc3wgQUMNCiAgICBBQyAtLi0+fEFrdHVhbGlzaWVydHwgQ1YNCiAgICBDViAtLi0+fExpZXN0IERhdGVufCBURA0K)

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
