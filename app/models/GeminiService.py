"""
Model - AI Service (Datenquelle)
Dies ist Teil des Models, da es externe Daten bereitstellt
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv


class GeminiService:
    """Singleton Service für AI-Anfragen"""
    
    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GeminiService, cls).__new__(cls)
            load_dotenv()
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("API Key fehlt in .env!")

            genai.configure(api_key=api_key)
            cls._model = genai.GenerativeModel('gemini-2.5-flash')
        return cls._instance

    def fetch_suggestions(self, city: str, vibe: str) -> str:
        """
        Holt Reiseempfehlungen von der AI
        
        Args:
            city: Name der Stadt
            vibe: Gewünschte Atmosphäre
            
        Returns:
            String mit Empfehlungen oder Fehlermeldung
        """
        prompt = (
            f"Erstelle 3 kurze Reisetipps für {city} mit dem Fokus auf "
            f"'{vibe}'. Format: Nur eine Liste."
        )
        try:
            response = self._model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Fehler bei AI-Anfrage: {e}"