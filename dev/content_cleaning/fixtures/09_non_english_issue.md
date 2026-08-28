# Zeitzonenberechnung liefert falsches Ergebnis bei Sommerzeitumstellung

State: CLOSED | #9009
Labels: bug

---

### Beschreibung des Fehlers

Wenn ich `convert_timezone("Europe/Berlin", "UTC")` genau am Tag der Umstellung von Winter- auf
Sommerzeit aufrufe, bekomme ich ein um eine Stunde falsches Ergebnis zurück. An allen anderen
Tagen funktioniert es korrekt.

### Wie kann man den Fehler reproduzieren

```python
from mypkg import convert_timezone
from datetime import datetime

dt = datetime(2024, 3, 31, 2, 30)
result = convert_timezone(dt, "Europe/Berlin", "UTC")
print(result)
```

Erwartet: `2024-03-31 00:30:00+00:00`
Tatsächlich: `2024-03-31 01:30:00+00:00`

# Comments on example/repo#9009

Total: 2 comments

--- Comment 1 ---

Das ist eine klassische "nicht existierende Zeit" — 2:30 Uhr existiert an diesem Tag in Berlin
gar nicht, die Uhr springt direkt von 2:00 auf 3:00. Die Bibliothek, die wir intern für die
Zeitzonenumrechnung benutzen, rundet solche nicht-existierenden Zeiten stillschweigend ab,
anstatt einen Fehler zu werfen. Das sollten wir ändern.

--- Comment 2 ---

Guter Punkt. Ich werde einen Pull Request öffnen, der bei nicht-existierenden lokalen Zeiten
eine `NonExistentTimeError` wirft, anstatt stillschweigend zu runden. Das ist zwar ein
Breaking Change, aber ein stiller falscher Wert ist schlimmer als eine laute Exception.
