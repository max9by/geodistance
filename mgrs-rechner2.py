# Funktioniert nur mit Pythen 3.12
import math
from mgrs import MGRS as MGRS

def mgrs_to_latlon(cmgrs: str):
    """Konvertiert eine MGRS-Koordinate in (lat, lon)."""
    m = MGRS()
    return m.toLatLon(cmgrs)

def haversine_distance(lat1, lon1, lat2, lon2):
    """Berechnet die Distanz zwischen zwei Lat/Lon-Punkten in Metern."""
    R = 6378137.0  # WGS84-Radius in Meter
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def mgrs_distance(cmgrs1: str, cmgrs2: str):
    """Berechnet den Abstand zwischen zwei MGRS-Punkten in Zentimetern."""
    lat1, lon1 = mgrs_to_latlon(cmgrs1)
    lat2, lon2 = mgrs_to_latlon(cmgrs2)
    dist_m = haversine_distance(lat1, lon1, lat2, lon2)
    return dist_m * 100  # Zentimeter

if __name__ == "__main__":
    print("Abstand zwischen zwei MGRS-Koordinaten (Genauigkeit bis auf Zentimeter)\n")
    while True:
        p1 = input("Gib MGRS für Punkt 1 ein (z. B. 33UXP0439685028): ").strip()
        p2 = input("Gib MGRS für Punkt 2 ein (z. B. 33UXP0440685033): ").strip()
        try:
            dist_cm = mgrs_distance(p1, p2)
        except Exception as e:
            print(f"Fehler: {e}")
        else:
            print(f"Der Abstand beträgt: {dist_cm:.0f} Zentimeter ({dist_cm/100:.2f} Meter)")
        print("\n--- Neu starten oder STRG+C zum Beenden ---\n")

