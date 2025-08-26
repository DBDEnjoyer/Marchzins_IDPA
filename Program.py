from datetime import datetime

def berechne_marchzins(kapital: float, zinssatz: float, geburtstag: str) -> float:
    """
    Berechnet den Marchzins-Bonus.
    
    :param kapital: Sparkapital in CHF
    :param zinssatz: Zinssatz in Prozent (z.B. 1.5)
    :param geburtstag: Geburtstag im Format 'TT.MM'
    :return: Marchzins-Bonus in CHF
    """
    tag, monat = map(int, geburtstag.split("."))
    
    tage = tag  
    
    
    zins = (kapital * zinssatz * tage) / (360 * 100)
    return round(zins, 2)


print(berechne_marchzins(10000, 1.5, "15.03"))  
