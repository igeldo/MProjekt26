"""
Model - Datenstrukturen und Geschäftslogik
"""

class TripData:
    """Datenmodell für Reiseinformationen"""
    
    def __init__(self):
        self.city: str = ""
        self.vibe: str = ""
        self.recommendations: str = ""

    def clear(self):
        """Setzt alle Daten zurück"""
        self.city = ""
        self.vibe = ""
        self.recommendations = ""
    
    def is_city_valid(self, city: str) -> bool:
        """Validiert Stadt-Eingabe"""
        return bool(city and city.strip())
    
    def is_end_command(self, city: str) -> bool:
        """
        Prüft, ob die Eingabe das Beenden-Kommando ist.

        Args:
            city (str): Die eingegebene Stadt.

        Returns:
            bool: True, wenn 'ende' (case-insensitive) eingegeben wurde.
        """
        return city.lower() == 'ende'
    
    def set_city(self, city: str):
        """Setzt die Stadt"""
        self.city = city.strip()
    
    def set_vibe_from_choice(self, choice: str) -> bool:
        """
        Konvertiert die Benutzereingabe in einen konkreten Vibe.

        Args:
            choice (str): Die Eingabe des Benutzers (z.B. "1", "2").

        Returns:
            bool: True, wenn eine gültige Wahl getroffen wurde, sonst False.
        """
        vibe_map = {
            "1": "Action & Abenteuer",
            "Action": "Action & Abenteuer",
            "2": "Ruhe & Entspannung",
            "Entspannung": "Ruhe & Entspannung"
        }
        
        if choice in vibe_map:
            self.vibe = vibe_map[choice]
            return True
        return False
    
    def set_recommendations(self, recommendations: str):
        """Setzt die AI-Empfehlungen"""
        self.recommendations = recommendations