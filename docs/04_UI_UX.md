# UI/UX Design Brief

## Aesthetic Direction
Functional prototype aesthetic — Tkinter's default system look (grey native widgets on Windows/macOS/Linux). No custom styling; the focus is entirely on the routing logic demonstration. Looks like a standard desktop utility application from the early 2000s, which is appropriate for a proof-of-concept demo in an academic or hackathon context.

## Color Palette
- Background: system default gray (Tkinter default)
- Text: system default black
- Buttons: system default (platform-native look)
- Output text widget: white background with black text
- No custom colors applied

## Typography
- Helvetica 14pt Bold for the title label
- Helvetica 12pt for section headers
- Default Tk font for form labels, dropdowns, and output text

## Component Style
- **Title label**: `"🚗 AutoPilot 5G - Routing Demo"` — top-centered, bold Helvetica 14pt
- **Form frame**: `ttk.Label` + `ttk.Combobox`/`ttk.Entry` pairs in a 3×2 grid
- **Add Vehicle button**: `ttk.Button`, spans full form width
- **Output label**: `"🧠 Suggested Routing Order:"` — section header
- **Output text widget**: `tk.Text` — 10 rows × 50 chars, scrollable text area displaying routed vehicles

## Dark / Light Mode
System default only — Tkinter inherits the OS appearance. No custom dark/light toggle.

## Reference Apps
- Legacy Windows utilities (Task Manager, Device Manager — same native Tkinter aesthetic)
- University lab simulation GUIs

## Key UI Patterns
- **Form + output split**: top half is input form, bottom half is output display
- **Combobox for vehicle type**: ensures only valid vehicle types can be selected
- **Text widget for output**: multi-line display, automatically updated on every vehicle add
- **Warning dialog**: `messagebox.showwarning` for missing fields — blocking popup

## Mobile Responsiveness
Not applicable — desktop Tkinter app only. Fixed 450×450 window size.

## Accessibility
- Native tkinter widgets are keyboard navigable (Tab between fields)
- Labels use descriptive text for each field
- Warning dialogs use messagebox (accessible to screen readers via OS accessibility APIs)
- No custom ARIA or accessibility enhancements
