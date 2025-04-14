import tkinter as tk
from tkinter import ttk, messagebox

# Vehicle speed mapping (higher = faster)
VEHICLE_SPEEDS = {
    "Ambulance": 100,
    "Scooty": 40,
    "Car": 60,
    "Truck": 30
}

# Multiple routes for each source-destination pair (4 routes for each pair)
ROUTES = {
    "A → B": ["Route 1", "Route 2", "Route 3", "Route 4"],
    "B → C": ["Route 1", "Route 2", "Route 3", "Route 4"],
    "C → D": ["Route 1", "Route 2", "Route 3", "Route 4"],
}

vehicles = []

def add_vehicle():
    # Get vehicle type, source, and destination from user input
    v_type = vehicle_type_var.get()
    source = source_var.get()
    destination = destination_var.get()

    # Check if all fields are filled
    if v_type == "" or source == "" or destination == "":
        messagebox.showwarning("Missing Info", "Please fill all fields.")
        return

    # Get the speed of the selected vehicle
    speed = VEHICLE_SPEEDS[v_type]
    eta = round(100 / speed, 2)  # Fake distance of 100 units

    # Try to assign a route to the vehicle
    route_assigned = None

    # Check if the source-destination pair already has a vehicle
    for v in vehicles:
        if v["Source"] == source and v["Destination"] == destination:
            route_assigned = "No available routes, rerouted"
            destination = f"{destination} (rerouted)"
            break

    # If no rerouted vehicle, assign a valid route from available ones
    if route_assigned is None:
        # Get all routes for this source-destination pair
        available_routes = ROUTES.get(f"{source} → {destination}", [])
        
        # Find the first available route that is not already taken
        for route in available_routes:
            if not any(v["Route"] == route for v in vehicles):
                route_assigned = route
                break

    # If no route was assigned (and no rerouting occurred), reroute the vehicle
    if route_assigned is None:
        if v_type == "Ambulance":
            route_assigned = "Route 1"  # Ambulance gets first priority
        else:
            route_assigned = "No available routes, rerouted"
            destination = f"{destination} (rerouted)"

    # Add the vehicle to the list
    vehicles.append({
        "Type": v_type,
        "Source": source,
        "Destination": destination,
        "Speed": speed,
        "ETA": eta,
        "Route": route_assigned
    })

    # Update the output
    update_output()

def update_output():
    # Sort vehicles: Ambulance gets priority, then based on ETA
    sorted_vehicles = sorted(vehicles, key=lambda x: (x["Type"] != "Ambulance", x["ETA"]))
    output_text.delete("1.0", tk.END)
    for v in sorted_vehicles:
        line = f'{v["Type"]} | {v["Source"]} → {v["Destination"]} | Route: {v["Route"]} | ETA: {v["ETA"]} min\n'
        output_text.insert(tk.END, line)

def clear_fields():
    vehicle_type_var.set("")
    source_var.set("")
    destination_var.set("")

# GUI Setup
root = tk.Tk()
root.title("AutoPilot 5G - Prototype")
root.geometry("450x450")

title = tk.Label(root, text="🚗 AutoPilot 5G - Routing Demo", font=("Helvetica", 14, "bold"))
title.pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack()

vehicle_type_var = tk.StringVar()
source_var = tk.StringVar()
destination_var = tk.StringVar()

ttk.Label(form_frame, text="Vehicle Type:").grid(row=0, column=0, sticky="e")
ttk.Combobox(form_frame, textvariable=vehicle_type_var, values=list(VEHICLE_SPEEDS.keys())).grid(row=0, column=1)

ttk.Label(form_frame, text="Source:").grid(row=1, column=0, sticky="e")
ttk.Entry(form_frame, textvariable=source_var).grid(row=1, column=1)

ttk.Label(form_frame, text="Destination:").grid(row=2, column=0, sticky="e")
ttk.Entry(form_frame, textvariable=destination_var).grid(row=2, column=1)

ttk.Button(form_frame, text="Add Vehicle", command=add_vehicle).grid(row=3, columnspan=2, pady=10)

output_label = tk.Label(root, text="🧠 Suggested Routing Order:", font=("Helvetica", 12))
output_label.pack()

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()
