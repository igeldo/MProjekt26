"""
View - Konsolenausgabe und Benutzereingabe
Nur für Darstellung und Input zuständig, keine Logik!
"""

class ConsoleView:
    """View für Konsolen-basierte Interaktion"""
    
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

    def show_results(self, city: str, recommendations: str):
        """Zeigt Ergebnisse an"""
        print(f"\n--- Tipps für {city} ---")
        print(recommendations)
        print("------------------------")

    def show_error(self, message: str):
        """Zeigt Fehlermeldung"""
        print(f"!!! {message} !!!")
    
    def show_goodbye(self):
        """Zeigt Abschiedsnachricht"""
        print("Kein Problem, wir sehen uns beim nächsten Mal!")