from app.model.TripData import TripData
from app.model.GeminiService import GeminiService
from app.view.ConsoleView import ConsoleView


class AppController:
    """
    Controller-Klasse für die Anwendungslogik.
    Verbindet Model und View und steuert den Hauptablauf.
    """

    def __init__(self):
        # Model initialisieren
        self.data = TripData()
        self.ai_service = GeminiService()

        # View initialisieren mit Model-Referenz
        self.view = ConsoleView(self.data)

        # Zustand
        self.running = True

    def run(self):
        """Hauptschleife der Anwendung"""
        while self.running:
            self.view.show_welcome()

            # Stadt-Eingabe
            if not self.handle_city_input():
                break  # Beenden gewünscht

            # Vibe-Auswahl
            if not self.handle_vibe_input():
                continue  # Zurück zum Start

            # Empfehlungen holen
            self.handle_recommendations()

            # Für nächste Runde vorbereiten
            self.data.clear()

    def handle_city_input(self) -> bool:
        """
        Verarbeitet die Eingabe der Stadt.
        Prüft auf Beenden-Kommando und Validität.

        Returns:
            bool: True, wenn der Programmfluss fortgesetzt werden soll.
                  False, wenn das Programm beendet werden soll.
        """
        while True:
            city = self.view.get_city_input()

            # Beenden-Kommando prüfen
            if self.data.is_end_command(city):
                self.view.show_goodbye()
                self.running = False
                return False

            # Validierung
            if not self.data.is_city_valid(city):
                self.view.show_error("Bitte eine Stadt eingeben!")
                continue

            # Daten speichern
            self.data.set_city(city)
            return True

    def handle_vibe_input(self) -> bool:
        """
        Verarbeitet die Auswahl des Vibes.

        Returns:
            bool: True, wenn eine gültige Auswahl getroffen wurde.
                  False, wenn die Auswahl ungültig war (wiederholen).
        """
        while True:
            choice = self.view.get_vibe_input()

            # Validierung und Speicherung über Model
            if self.data.set_vibe_from_choice(choice):
                return True

            self.view.show_error("Ungültige Wahl. Bitte 1 oder 2 wählen.")

    def handle_recommendations(self):
        """Holt und zeigt Empfehlungen"""
        self.view.show_loading()

        # AI-Service über Model nutzen
        recommendations = self.ai_service.fetch_suggestions(
            self.data.city,
            self.data.vibe
        )

        # Ergebnis im Model speichern
        self.data.set_recommendations(recommendations)

        # View zeigt Daten direkt aus Model an
        self.view.show_results()