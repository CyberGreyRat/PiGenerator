import sys

def pi_stream():
    """
    Ein Generator, der Pi Ziffer für Ziffer ausspuckt.
    Basierend auf den Algorithmen von Jeremy Gibbons.
    Das ist ein 'Unbounded Spigot Algorithm'.
    """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    
    while True:
        if 4 * q + r - t < n * t:
            # Wir haben eine sichere Ziffer gefunden!
            yield n
            
            # Mathematik für den nächsten Schritt (Ziffer 'vergessen', neue vorbereiten)
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            # Wir sind noch nicht sicher, wir müssen genauer rechnen
            nr = (2 * q + r) * l
            nn = (q * (7 * k + 2) + r * l) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

# --- HAUPTPROGRAMM ---
if __name__ == "__main__":
    print("Starte unendlichen Pi-Stream... (STRG+C zum Abbrechen)")
    
    # Zähler für die Statistik
    count = 0
    
    try:
        # Wir holen uns Ziffer für Ziffer aus dem Generator
        for digit in pi_stream():
            
            # Die erste Ziffer ist die 3, danach kommt der Punkt
            if count == 0:
                sys.stdout.write(str(digit) + ".")
            else:
                sys.stdout.write(str(digit))
            
            # Damit man es live sieht (Puffer leeren)
            sys.stdout.flush()
            
            count += 1
            
            # Optional: Zeilenumbruch alle 100 Zahlen (damit es hübsch bleibt)
            # if count % 100 == 0:
            #    sys.stdout.write("\n")
            
    except KeyboardInterrupt:
        print(f"\n\n--- Abgebrochen bei {count} Stellen ---")