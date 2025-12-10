from collections import Counter
import matplotlib.pyplot as plt # Falls du Diagramme willst (muss installiert sein: pip install matplotlib)
# Falls kein matplotlib da ist, nutzen wir Text-Balken

def analysiere_pi():
    filename = "pi_live.txt"
    try:
        with open(filename, "r") as f:
            content = f.read()
            digits = content.replace("3.", "").replace("\n", "")
            
        total = len(digits)
        print(f"Analysiere {total} Stellen...\n")
        
        # Zähle alle Ziffern
        counts = Counter(digits)
        
        print("Ziffer | Anzahl | Prozent | Balkendiagramm")
        print("-" * 50)
        
        for ziffer in "0123456789":
            anzahl = counts[ziffer]
            prozent = (anzahl / total) * 100
            # Ein simpler Text-Balken (1 Strich pro 0.5 Prozent)
            balken = "#" * int(prozent * 2) 
            print(f"   {ziffer}   | {anzahl:6d} | {prozent:5.2f}% | {balken}")
            
    except FileNotFoundError:
        print("Bitte erst pi_live.txt erstellen!")

if __name__ == "__main__":
    analysiere_pi()