# PRD — Product Requirements Document

## App Name
AutoPilot 5G — Routing Demo

## Tagline
A desktop GUI prototype demonstrating 5G-assisted autonomous vehicle routing with priority-based lane and route assignment.

## Problem
Traditional traffic routing systems treat all vehicles equally. Emergency vehicles like ambulances are delayed by the same routing queues as regular vehicles, costing lives. This prototype demonstrates how a 5G-connected autopilot system could intelligently prioritize emergency vehicles, assign dedicated routes, and calculate ETAs based on vehicle type — all in real time.

## Target User
**Primary:** Engineering students, researchers, and hackathon participants demonstrating 5G smart city or autonomous vehicle concepts. They need a visual prototype that illustrates routing intelligence without requiring real hardware or network infrastructure.  
**Secondary:** Professors and evaluators reviewing a proof-of-concept for 5G-assisted autonomous vehicle management.

## Core Features (Must Have)
- Select vehicle type from dropdown: Ambulance, Scooty, Car, Truck
- Select source and destination from predefined nodes (A, B, C, D)
- Add vehicle to routing table — system assigns the next available route from 4 possible routes per source-destination pair
- Ambulance always gets Route 1 (highest priority) regardless of availability
- ETA calculation based on vehicle speed: Ambulance 100 km/h → 1.0 min, Car 60 km/h → 1.67 min, Scooty 40 km/h → 2.5 min, Truck 30 km/h → 3.33 min (calculated over fake distance of 100 units)
- If all routes for a source-destination pair are taken, new vehicles are marked "rerouted" with destination label updated
- Output display: sorted list — Ambulances first, then ascending ETA order
- Clear fields button after adding a vehicle
- Tkinter GUI: runs as a native desktop window (no browser needed)

## Nice to Have
- Real map visualization with actual road network
- Live simulation mode: vehicles move along routes in real time
- Dynamic route capacity (more than 4 routes per pair)
- Traffic density simulation affecting ETAs
- Network packet visualization representing 5G communication between vehicles
- Export routing log to CSV

## Out of Scope
- Actual 5G network integration
- GPS or map API usage
- Multi-city routing
- Real hardware or vehicle simulation

## User Stories
- As a **demo presenter**, I want to add an Ambulance and show it jumping to Route 1 regardless of other vehicles so that I can demonstrate priority routing to the audience.
- As a **student**, I want to add multiple vehicles and see the sorted output (ambulances first, then by ETA) so that the routing intelligence is visually clear.
- As a **researcher**, I want to see vehicles marked as "rerouted" when all routes are taken so that the system's fallback behavior is demonstrable.

## Success Metrics
- GUI launches within 2 seconds on any Python 3.x installation
- Vehicle routing priority (Ambulance first) visually demonstrable in < 10 seconds of demo
- No crashes when all 4 routes for a pair are occupied
- Sorting order correct: Ambulance always on top, then ascending ETA
