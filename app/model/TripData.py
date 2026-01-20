"""
Model - Datenstrukturen und Geschäftslogik
"""

class TripData:
    """Datenmodell für Reiseinformationen"""
    
    def __init__(self):
        self.city: str = ""
        self.group_size: int = 1
        self.vibe: str = ""
        self.recommendations: str = ""

    def clear(self):
        """Setzt alle Daten zurück"""
        self.city = ""
        self.group_size = 1
        self.vibe = ""
        self.recommendations = ""
    
    def is_city_valid(self, city: str) -> bool:
        """Validiert Stadt-Eingabe"""
        return bool(city and city.strip())
    
    def is_end_command(self, city: str) -> bool:
        """Prüft ob Beenden-Kommando"""
        return city.lower() == 'ende'
    
    def set_city(self, city: str):
        """Setzt die Stadt"""
        self.city = city.strip()

    def set_group_size(self, size_input: str) -> bool:
       
        try:
            val = int(size_input)
            if val > 0:
                self.group_size = val
                return True
            return False
        except ValueError:
            return False
    
    def set_vibe_from_choice(self, choice: str) -> bool:
        """
        Konvertiert User-Wahl zu Vibe
        Returns: True wenn gültig, False sonst
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