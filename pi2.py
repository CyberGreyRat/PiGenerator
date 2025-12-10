import sys

# Das ist wieder der Generator (der Mathe-Teil)
def pi_stream():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k + 2) + r * l) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

# --- HIER IST DER NEUE TEIL ---
if __name__ == "__main__":
    dateiname = "pi_live.txt"
    
    print(f"--- PI GENERATOR GESTARTET ---")
    print(f"Speichere Zahlen in Datei: {dateiname}")
    print("Druecke STRG+C zum Stoppen.\n")

    # Wir öffnen die Datei im Schreib-Modus ("w")
    with open(dateiname, "w") as f:
        count = 0
        
        try:
            for digit in pi_stream():
                # 1. In die Datei schreiben
                if count == 0:
                    f.write(str(digit) + ".") # Die 3 und der Punkt
                else:
                    f.write(str(digit))       # Nur die Ziffer
                
                count += 1

                # 2. Live-Anzeige auf dem Bildschirm (alle 100 Stellen)
                # Wir machen das nur alle 100 Stellen, damit der PC nicht
                # vom ständigen "Drucken" ausgebremst wird.
                if count % 100 == 0:
                    # \r springt an den Zeilenanfang zurück -> Überschreibt die alte Zahl
                    sys.stdout.write(f"\r>> Aktuelle Anzahl Stellen: {count}")
                    sys.stdout.flush()
                    
                    # Wichtig: Speichern erzwingen, damit bei Absturz nichts fehlt
                    f.flush()
                    
        except KeyboardInterrupt:
            print(f"\n\nSTOPP! Datei wurde gespeichert.")
            print(f"Du hast {count} Stellen von Pi gesammelt.")
            print(f"Schau in '{dateiname}' nach!")