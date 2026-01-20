from app.controller.AppController import AppController


def main():
    """Hauptfunktion - startet die Anwendung"""
    try:
        # Controller erstellen und starten
        app = AppController()
        app.run()

    except KeyboardInterrupt:
        # Strg+C wurde gedrückt
        print("\n\nAnwendung wurde beendet.")

    except Exception as e:
        # Unerwarteter Fehler
        print(f"\n!!! Ein Fehler ist aufgetreten: {e} !!!")
        print("Bitte überprüfe deine .env Datei und Internetverbindung.")


if __name__ == "__main__":
    main()