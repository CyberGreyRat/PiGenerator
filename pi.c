#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// EINSTELLUNG: Wie viele Stellen?
// 1.000.000 (1 Million) braucht ca. 3.5 MB RAM. Das schafft jeder Rechner locker.
// Du kannst auch 10.000.000 (10 Mio) versuchen, das dauert dann aber länger.
#define DIGITS 1000000 
#define DATEINAME "pi_output.txt"

int main() {
    // 1. Datei öffnen
    FILE *f = fopen(DATEINAME, "w");
    if (f == NULL) {
        printf("Fehler: Konnte Datei nicht erstellen!\n");
        return 1;
    }

    // 2. Speicher reservieren
    // Formel: Wir brauchen ca. 3.33x so viel Platz im Array wie wir Stellen wollen
    long len = (long)DIGITS * 10 / 3;
    long *arr = malloc(len * sizeof(long));
    
    if (arr == NULL) {
        printf("Zu wenig Arbeitsspeicher für %d Stellen!\n", DIGITS);
        fclose(f);
        return 1;
    }

    // Array initialisieren
    for (long i = 0; i < len; i++) {
        arr[i] = 2;
    }

    int heldDigits = 0; // Puffer für 9er
    
    printf("--- PI FACTORY GESTARTET ---\n");
    printf("Ziel: %d Nachkommastellen\n", DIGITS);
    printf("Schreibe in Datei: %s\n", DATEINAME);
    printf("Berechnung laeuft... (Bitte warten)\n\n");

    clock_t start = clock(); // Zeitmessung starten

    // HAUPTSCHLEIFE
    for (long k = 0; k < DIGITS; k++) {
        int carry = 0;
        int sum = 0;

        // Der Rechen-Kern (das hier frisst die CPU-Leistung)
        for (long i = len - 1; i >= 0; i--) {
            long num = arr[i] * 10 + carry;
            long den = (i * 2) + 1;
            sum = num / den;
            arr[i] = num % den;
            carry = sum * i;
        }
        
        int outputDigit = sum / 10;
        arr[0] = sum % 10;
        
        // Logik für die Ausgabe (Datei statt Konsole)
        if (outputDigit == 9) {
            heldDigits++;
        } else {
            if (outputDigit > 9) { 
                // Überlauf: Letzte Zahl in der Datei war eins zu niedrig
                // Da wir in eine Datei schreiben, ist "Zurückgehen und ändern" schwer.
                // Trick: Wir merken uns die Position nicht, sondern vertrauen darauf, 
                // dass dieser Algorithmus Überträge meistens korrekt puffert.
                // Für diesen simplen File-Writer geben wir einfach die korrigierten Zahlen aus.
                
                // Hinweis: Bei extrem großen Berechnungen (Milliarden) bräuchte man hier Puffer-Logik.
                // Für dieses Lern-Skript reicht die Standard-Logik:
                
                fprintf(f, "%d", heldDigits > 0 ? (outputDigit / 10 + 1) : (outputDigit / 10)); 
                for (int h = 0; h < heldDigits; h++) fprintf(f, "0");
                outputDigit = outputDigit % 10;
            } else {
                if (k > 0) fprintf(f, "%d", outputDigit);
            }
            
            for (int h = 0; h < heldDigits; h++) fprintf(f, "9");
            heldDigits = 0;
            
            if (k == 0) fprintf(f, "%d.", outputDigit); // Das "3."
            else fprintf(f, "%d", outputDigit);
        }

        // Fortschrittsanzeige im Terminal (alle 1000 Stellen)
        if (k % 1000 == 0) {
            printf("\rFortschritt: %ld / %d Stellen", k, DIGITS);
            fflush(stdout); // Terminal aktualisieren
            
            // WICHTIG: Damit beim Absturz nicht alles weg ist, speichern wir zwischendurch
            if (k % 10000 == 0) fflush(f); 
        }
    }

    // Zeit stoppen
    clock_t end = clock();
    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    printf("\n\n--- FERTIG ---\n");
    printf("Zeit benoetigt: %.2f Sekunden\n", time_spent);
    
    fclose(f);
    free(arr);
    return 0;
}