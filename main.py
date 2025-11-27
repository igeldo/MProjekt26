# Zustand.py (oder in der gleichen Datei wie die Zustands-Klassen)

class Zustand:
    def __init__(self, x):
        self.x = x

    # ... (Methoden wie zuvor) ...
    def setX(self, x):
        raise NotImplementedError("Subclasses must implement setX method")

    def status(self):
        raise NotImplementedError("Subclasses must implement status method")


class ZustandOK(Zustand):
    def __init__(self, x):
        super().__init__(x)
        # Optional: Private Klassenvariable für Singleton-Verwaltung
        # (wird im Manager unten verwendet)
        self.__instance = None

    def setX(self, x):
        self.x = x
        # Wenn der Status wechselt, muss die neue Instanz vom Singleton Manager kommen
        if x >= 42:
            return StatusSingletonManager.Kritisch(x)
        else:
            return self

    def status(self):
        return "alles ok"


class ZustandKritisch(Zustand):
    def __init__(self, x):
        super().__init__(x)
        # Optional: Private Klassenvariable für Singleton-Verwaltung
        self.__instance = None

    def setX(self, x):
        self.x = x
        # Wenn der Status wechselt, muss die neue Instanz vom Singleton Manager kommen
        if x <= 22:
            return StatusSingletonManager.OK(x)
        else:
            return self

    def status(self):
        return "kritisch"


class StatusSingletonManager:
    """
    Entspricht der Java-Klasse 'Singleton'.
    Verwaltet die einzigen Instanzen von ZustandOK und ZustandKritisch.
    """
    # Private Klassenvariablen (entspricht den static private Variablen in Java)
    __p_ok = None
    __p_Krit = None

    @staticmethod
    def OK(x):
        """Stellt sicher, dass nur eine Instanz von ZustandOK existiert."""
        if StatusSingletonManager.__p_ok is None:
            StatusSingletonManager.__p_ok = ZustandOK(x)
        # Unabhängig von x wird immer dieselbe Instanz zurückgegeben.
        # Der x-Wert wird hier nur initial genutzt.
        return StatusSingletonManager.__p_ok

    @staticmethod
    def Kritisch(x):
        """Stellt sicher, dass nur eine Instanz von ZustandKritisch existiert."""
        if StatusSingletonManager.__p_Krit is None:
            StatusSingletonManager.__p_Krit = ZustandKritisch(x)
        # Unabhängig von x wird immer dieselbe Instanz zurückgegeben.
        return StatusSingletonManager.__p_Krit


# --- Beispielhafte Nutzung ---
if __name__ == "__main__":
    # Wir greifen jetzt über den Manager auf die Zustände zu, nicht mehr via new ZustandOK()

    # Initialisierung der OK-Instanz über den Manager
    state1 = StatusSingletonManager.OK(10)
    print(f"State 1 Status: {state1.status()}, x={state1.x}")

    # Initialisierung der Kritisch-Instanz über den Manager (selbst wenn wir hier x=500 übergeben,
    # wird beim zweiten Aufruf die gleiche Instanz von oben zurückgegeben, x bleibt 10,
    # es sei denn, wir rufen explizit .setX() auf der Instanz auf.)
    state2 = StatusSingletonManager.Kritisch(45)
    print(f"State 2 Status: {state2.status()}, x={state2.x}")

    # Test, ob es sich um dieselben Objekte handelt (Identitätsprüfung)
    state1_again = StatusSingletonManager.OK(999)  # x=999 wird ignoriert, da Instanz schon existiert
    print(f"\nIst state1_again identisch mit state1? {state1_again is state1}")
    print(f"Aktueller x-Wert von state1: {state1.x}\n")

    # Wenn wir den Zustand *ändern* und dabei die Singleton-Logik nutzen wollen:
    # Wir übergeben den Wert, die setX-Methode entscheidet über den *Rückgabe*-Typ (das Singleton-Objekt)
    current_state = StatusSingletonManager.OK(20)
    print(f"Current state: {current_state.status()}")

    # Wechsel zu kritisch: setX gibt das Singleton-Objekt für 'Kritisch' zurück
    current_state = current_state.setX(45)
    print(f"Current state nach setX(45): {current_state.status()}")
    print(f"Ist der neue Zustand das 'Kritisch'-Singleton? {current_state is StatusSingletonManager.Kritisch(0)}")
