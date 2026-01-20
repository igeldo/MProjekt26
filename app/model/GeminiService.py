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
            cls._model = genai.GenerativeModel('gemini-2.5-flash-lite')
        return cls._instance

    def fetch_suggestions(self, city: str, group_size: int, vibe: str) -> str:
        """
        Holt Reisevorschläge von der Google Gemini API.
    """
        prompt = (
            f"Du bist ein Reiseexperte. Erstelle 3 konkrete Reisetipps für {city}, "
            f"die exakt auf eine Gruppe von {group_size} Personen zugeschnitten sind. "
            f"Vibe: '{vibe}'. "
            f"WICHTIG: Erkläre bei jedem Tipp kurz in Klammern, warum er gerade für {group_size} Personen ideal ist "
            f"(z.B. 'romantisch zu zweit' oder 'lustig als große Truppe'). "
            f"Vermeide generische Vorschläge, die immer passen."
        )
        try:
            response = self._model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Fehler bei AI-Anfrage: {e}"