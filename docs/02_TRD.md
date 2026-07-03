# TRD — Technical Requirements Document

## Frontend
- Python tkinter — native desktop GUI (included in Python standard library)
- ttk widgets: Combobox (dropdowns), Entry (text input), Button, Label, Text (output area)
- No web browser required — runs as a standalone Python desktop application

## Backend
None — all logic runs in the same Python process as the GUI.

## Database
None — vehicle list stored in an in-memory Python list (`vehicles = []`). Cleared when the app is closed.

## Authentication
None.

## Hosting
Run locally: `python prototype.py`. No server, no deployment.

## Third-party APIs & Services
None — fully offline. No network calls.

## Key Libraries
- `tkinter` — Python standard library GUI framework (no install required)
- `tkinter.ttk` — themed widget set (Combobox, Label, Button)
- `tkinter.messagebox` — popup warnings for missing input

## Environment Variables
None.

## Constraints
- Vehicle speed values are hardcoded: Ambulance 100, Car 60, Scooty 40, Truck 30 (km/h)
- ETA formula: `round(100 / speed, 2)` — assumes fixed distance of 100 units for all routes
- Route table hardcoded: only `A → B`, `B → C`, `C → D` pairs supported (4 routes each)
- Ambulance always assigned Route 1 regardless of other vehicles (priority hardcoded in logic)
- If all 4 routes for a pair are taken, vehicle is marked "rerouted" with destination suffixed `(rerouted)`
- GUI window fixed at 450×450 pixels
- Output sorted on every update: Ambulance first (`Type != "Ambulance"` sort key), then ascending ETA
- No persistence — restarting the app clears all vehicles
- Requires Python 3.x with tkinter (pre-installed on most systems; on some Linux distros requires `sudo apt install python3-tk`)
