# 🥧 Infinite Pi Project

**Eine Reise in die Unendlichkeit: Algorithmen zur Berechnung von Pi mit beliebiger Genauigkeit.**

Dieses Projekt ist eine Sammlung von Experimenten und Implementierungen, um die Grenzen der computergestützten Mathematik zu testen. Es demonstriert verschiedene Ansätze – von visuellen Darstellungen im Browser bis hin zu High-Performance-Berechnungen in C – um die Kreiszahl Pi ($\pi$) auf Tausende oder Millionen von Nachkommastellen genau zu berechnen.

---

## 🚀 Übersicht der Module

Dieses Repository enthält drei verschiedene Implementierungen, die jeweils unterschiedliche Konzepte der Informatik beleuchten:

### 1. 🐍 Python: Der Unendliche Stream (`pi.py`)
Ein **Unbounded Spigot Algorithmus** (basierend auf Jeremy Gibbons), der als Generator arbeitet.
* **Konzept:** "Lazy Evaluation" – Es wird immer nur die nächste Ziffer berechnet.
* **Features:**
    * Gleichzeitige Ausgabe in Konsole (Live-Counter) und Datei.
    * Extrem speichereffizient (kein riesiges Array im RAM nötig).
    * Tools zur Analyse: `pi_stats.py` prüft die statistische Verteilung der Ziffern 0-9.

### 2. ⚡ C: High-Performance Computing (`pi.c`)
Eine Implementierung des **Spigot-Algorithmus** für maximale Rechengeschwindigkeit.
* **Konzept:** Direkte Speicherverwaltung und Integer-Arithmetik.
* **Performance:** Berechnet 1.000.000 Stellen in wenigen Minuten.
* **Technik:** Nutzt `malloc`/`free` für große Arrays und optimierte Loops ($O(n^2)$).

### 3. 🌐 JavaScript: Visualisierung (`indec.html`)
Eine visuelle Darstellung der Berechnung basierend auf **Ramanujans Formel (1914)**.
* **Konzept:** Arbitrary Precision im Browser mittels `Decimal.js`.
* **Visualisierung:** Matrix-Style Effekt, bei dem Ziffern einzeln erscheinen, sobald sie mathematisch stabil sind.
* **Lerneffekt:** Umgang mit dem Event-Loop (nicht blockierende UI) und großen Zahlen in JS.

---

"Die Mathematik ist das Alphabet, mit dessen Hilfe Gott das Universum beschrieben hat." - Galileo Galilei
