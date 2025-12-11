"""
View - Konsolenausgabe und Benutzereingabe
Liest Daten direkt aus dem Model für die Darstellung
"""


class ConsoleView:
    """View für Konsolen-basierte Interaktion"""

    def __init__(self, model):
        """
        Initialisiert View mit Referenz zum Model

        Args:
            model: TripData Instanz
        """
        self.model = model

    def show_welcome(self):
        """Zeigt Willkommensnachricht"""
        print("\n=== Aktivitäten-PLANER ===")
        print("Lass uns deinen perfekten Tag planen.")

    def get_city_input(self) -> str:
        """Holt Stadt-Eingabe vom Benutzer"""
        return input(
            "\nBitte gib deinen Ausflugsort ein (oder 'Ende' für Ende): "
        ).strip()

    def get_vibe_input(self) -> str:
        """Holt Stimmungs-Auswahl vom Benutzer"""
        print("\nWorauf hast du Lust?")
        print("1: Action")
        print("2: Entspannung")
        return input("Deine Wahl: ").strip()

    def show_loading(self):
        """Zeigt Ladeanzeige"""
        print("... Antwort wird erstellt ...")

    def show_results(self):
        """
        Zeigt Ergebnisse an - holt Daten direkt aus dem Model
        """
        print(f"\n--- Tipps für {self.model.city} ---")
        print(self.model.recommendations)
        print("------------------------")

    def show_error(self, message: str):
        """Zeigt Fehlermeldung"""
        print(f"!!! {message} !!!")

    def show_goodbye(self):
        """Zeigt Abschiedsnachricht"""
        print("Kein Problem, wir sehen uns beim nächsten Mal!")