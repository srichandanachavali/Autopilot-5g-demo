# Backend Schema — Data Model & Auth Architecture

## Database Tables
None — all data in Python in-memory list.

## Data Model (in-memory)

### `vehicles` list
Global Python list. Each entry is a dict:
```python
{
    "Type": str,         # "Ambulance" | "Scooty" | "Car" | "Truck"
    "Source": str,       # e.g. "A"
    "Destination": str,  # e.g. "B" or "B (rerouted)"
    "Speed": int,        # from VEHICLE_SPEEDS lookup
    "ETA": float,        # round(100 / speed, 2)
    "Route": str         # "Route 1" | "Route 2" | ... | "No available routes, rerouted"
}
```

### `VEHICLE_SPEEDS` constant
```python
{
    "Ambulance": 100,
    "Scooty": 40,
    "Car": 60,
    "Truck": 30
}
```

### `ROUTES` constant
```python
{
    "A → B": ["Route 1", "Route 2", "Route 3", "Route 4"],
    "B → C": ["Route 1", "Route 2", "Route 3", "Route 4"],
    "C → D": ["Route 1", "Route 2", "Route 3", "Route 4"],
}
```

## Routing Logic
1. Check if any existing vehicle has same Source + Destination → if yes, mark new vehicle as rerouted
2. If not rerouted, find first route in `ROUTES[f"{source} → {destination}"]` not already in use
3. If all routes taken and vehicle is Ambulance → force Route 1 (priority override)
4. If all routes taken and not Ambulance → mark as rerouted

## Relationships
None.

## Auth Provider
None.

## Row Level Security
None.

## User Roles
None.

## Sensitive Fields
None.

## File Storage
None.

## API Endpoints
None — offline desktop app. No HTTP calls.
