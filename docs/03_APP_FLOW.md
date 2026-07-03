# App Flow — Navigation & User Journey Map

## Pages / Screens
Single window: `prototype.py` opens one Tkinter window (450×450 px) titled "AutoPilot 5G - Prototype".

## Navigation Structure
No navigation — single window with all controls visible at once.

## Entry Point
`python prototype.py` → Tkinter main loop starts → window opens.

## Auth Flow
None.

## Core User Journey 1 — Route an Ambulance (Priority Demo)
1. Run `python prototype.py`
2. Window opens with title "🚗 AutoPilot 5G - Routing Demo"
3. Select Vehicle Type: "Ambulance" from Combobox
4. Enter Source: "A"
5. Enter Destination: "B"
6. Click "Add Vehicle" button
7. `add_vehicle()` fires: gets Ambulance speed (100), calculates ETA (1.0 min)
8. Route assignment: `ROUTES["A → B"] = ["Route 1", "Route 2", ...]` — Ambulance gets Route 1 regardless
9. Vehicle appended to `vehicles[]` list
10. `update_output()` fires: sorts vehicles (Ambulance first), renders in Text widget
11. Output shows: `Ambulance | A → B | Route: Route 1 | ETA: 1.0 min`
12. Fields cleared

## Core User Journey 2 — All Routes Taken → Rerouting
1. Add 4 vehicles (e.g. 4 Cars) from A → B, consuming Route 1 through Route 4
2. Add a 5th Car from A → B
3. System detects: first vehicle already exists for this source-destination pair → marks as "rerouted"
4. Destination becomes "B (rerouted)", Route = "No available routes, rerouted"
5. Output shows the rerouted vehicle sorted by ETA in the appropriate position

## Empty States
- No vehicles added: Text widget shows blank output area
- Missing fields: `messagebox.showwarning("Missing Info", "Please fill all fields.")` popup

## Error States
- Empty vehicle type, source, or destination: warning dialog shown, vehicle not added
- No routes available for pair: vehicle rerouted with "(rerouted)" suffix on destination

## Redirects
None — desktop app, no routing.
