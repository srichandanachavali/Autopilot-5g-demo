# Implementation Plan

## Project Type
Python desktop prototype (Tkinter). Single-file application.

## Phase 1 — Core Routing Engine (Complete)
- [x] Define `VEHICLE_SPEEDS` and `ROUTES` constants
- [x] Implement route assignment logic with priority override for Ambulance
- [x] Implement rerouting logic when all routes are taken
- [x] Sort output by vehicle type priority (Ambulance first) then ETA

## Phase 2 — Tkinter UI (Complete)
- [x] Single 450×450 window with title "AutoPilot 5G - Prototype"
- [x] Form frame: Vehicle Type combobox, Source entry, Destination entry
- [x] "Add Vehicle" button triggering `add_vehicle()` and `update_output()`
- [x] Output text widget (10 rows × 50 chars) displaying routed vehicles
- [x] Warning dialog for missing fields via `messagebox.showwarning`

## Phase 3 — Enhancements (Future / Optional)
- [ ] Persist vehicle list to JSON file for session continuity
- [ ] Add "Clear All" button to reset `vehicles[]` list
- [ ] Add support for more route pairs (e.g. "D → E")
- [ ] Color-code vehicle types in output (requires `tk.Text` tag configuration)
- [ ] Expand to 5G network simulation: add signal strength, handoff events

## Stack
| Layer | Technology |
|-------|-----------|
| UI | Python 3 + Tkinter (ttk widgets) |
| Logic | Pure Python — no external libraries |
| Data | In-memory list (`vehicles[]`) |
| Entry point | `python prototype.py` |

## File Map
```
prototype.py     — entire app (UI + routing logic combined)
```

## Known Limitations
- No persistence — restarting clears all vehicles
- Fixed route pairs (A→B, B→C, C→D only)
- Rerouting check only looks at source+destination match, not route capacity globally
- JWT secret is hardcoded as `"secretkey"` — not applicable here (N/A for desktop)
