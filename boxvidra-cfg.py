import tkinter as tk
from tkinter import ttk
import subprocess
import threading

root = tk.Tk()
root.title("BOXVIDRA CFG")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "forest-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-dark")

# Create lists for the Comboboxes
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_listreso = ["1280x720", "1024x768", "800x600", "800x480", "640x480"]
combo_listwin = ["Windows 10 Theme (Light)", "Windows 10 Theme (Dark)", "Windows 10 Theme (Red, Gaming)", "Windows 10 Theme (Purple Space)", "Windows 7 Theme", "Windows XP Theme", "Windows 95 Theme"]
combo_listd = ["DXVK 2.3 Gpl-async", "DXVK 2.2 Gpl-async", "DXVK 2.0 Async", "DXVK 1.10.3 Async","DXVK 2.3","DXVK 2.2","DXVK 2.1","DXVK 1.9.4","DXVK 1.10.2","DXVK 1.10.1","DXVK-dev", "DXVK 1.6.1", "DXVK 0.96", "wined3d 8.20", "wined3d 8.02", "wined3d 7.21", "wined3d 7.8", "wined3d 7.2", "wined3d 4.13"]
combo_vddx = ["VDDX 2.0.1", "VDDX 1.10.0", "VDDX 1.0.0"]
combo_listmes = ["Turnip v8", "Turnip v7 (recommended)", "Turnip v6.5", "Turnip v5", "Turnip v4 (recommended)", "Turnip v3.5", "Turnip v3 (recommended)", "Turnip v2", "Virgl Mesa 24", "Virgl Mesa 22", "Virgl Mesa 19", "Virgl Mesa 18"]
combo_listbuilds = ["June12 Build (Not available)", "Not Available (20 June)", "Not Available (20 June)", "Not Available (20 June)", "Not Available (20 June)", "Not Available (20 June)"]
combo_startup = ["Wine programs (Desktop)", "Open Wine explorer (Not available)", "boxvidra startup (recommended)"]
combo_cores = ["2 Primary Cores", "3 Primary Cores", "4 Primary Core", "5 Primary Cores", "6 Primary Cores", "7 Primary Core"]

# Create control variables
a = tk.BooleanVar()
b = tk.BooleanVar(value=True)
c = tk.BooleanVar()
d = tk.IntVar(value=2)
v = tk.IntVar(value=2)
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()
t = tk.BooleanVar(value=True)

# Create a Frame for the Radiobuttons
radio_frame = ttk.LabelFrame(root, text="VIRGL SETTINGS", padding=(20, 10))
radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

# Define the function to execute when a radiobutton is selected
def on_radiobutton_selectvirgl():
    selectionvirgl = d.get()
    if selectionvirgl == 4:
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="GL 2.1 applied")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/virgl/virgl1.sh"])
        threading.Thread(target=run_command).start()

    elif selectionvirgl == 3:
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="GL 2.1 dxTn applied")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/virgl/virgl2.sh"])
        threading.Thread(target=run_command).start()
        
    elif selectionvirgl == 2:
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="GL 3.3 dxTn applied")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/virgl/virgl3.sh"])
        threading.Thread(target=run_command).start()

    elif selectionvirgl == 1:
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="GL 3.3 applied")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/virgl/virgl4.sh"])
        threading.Thread(target=run_command).start()

# Radiobuttons
radio_2 = ttk.Radiobutton(radio_frame, text="GL 2.1", variable=v, value=1, command=on_radiobutton_selectvirgl)
radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
radio_3 = ttk.Radiobutton(radio_frame, text="GL 2.1 dxTn (default)", variable=v, value=2, command=on_radiobutton_selectvirgl)
radio_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
radio_4 = ttk.Radiobutton(radio_frame, text="GL 3.3", variable=v, value=3, command=on_radiobutton_selectvirgl)
radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
radio_5 = ttk.Radiobutton(radio_frame, text="GL 3.3 dxTn", variable=v, value=4, command=on_radiobutton_selectvirgl)
radio_5.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")


# Separator
separator = ttk.Separator(root)
separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

# Create a Frame for the Radiobuttons
radio_frame = ttk.LabelFrame(root, text="HUD SETTINGS", padding=(20, 10))
radio_frame.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="nsew")

# Define the function to execute when a radiobutton is selected
def on_radiobutton_select():
    selection = d.get()
    if selection == 5:
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="DXVK HUD disabled")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/hud/disable-hud.sh"])
        threading.Thread(target=run_command).start()

    elif selection == 4:
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="DXVK SIMPLE HUD enabled")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/hud/simple-hud.sh"])
        threading.Thread(target=run_command).start()
        
    elif selection == 3:
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="DXVK HUD enabled")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/hud/dxvk-hud.sh"])
        threading.Thread(target=run_command).start()

    elif selection == 2:
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="MANGOHUD enabled")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/hud/mangohud-enable.sh"])
        threading.Thread(target=run_command).start()
        

    elif selection == 6:
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="MANGOHUD disabled")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/hud/mangohud-disable.sh"])
        threading.Thread(target=run_command).start()

# Radiobuttons
radio_2 = ttk.Radiobutton(radio_frame, text="Enable DXVK HUD", variable=d, value=2, command=on_radiobutton_select)
radio_2.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
radio_3 = ttk.Radiobutton(radio_frame, text="Enable Simple DXVK HUD", variable=d, value=3, command=on_radiobutton_select)
radio_3.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
radio_4 = ttk.Radiobutton(radio_frame, text="Disable DXVK HUD", variable=d, value=4, command=on_radiobutton_select)
radio_4.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")
radio_5 = ttk.Radiobutton(radio_frame, text="Enable MANGOHUD", variable=d, value=5, command=on_radiobutton_select)
radio_5.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
radio_6 = ttk.Radiobutton(radio_frame, text="Disable MANGOHUD", variable=d, value=6, command=on_radiobutton_select)
radio_6.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Combobox_Resolution 
combobox_resolution = ttk.Combobox(widgets_frame, values=combo_listreso)
combobox_resolution.current(0)
combobox_resolution.grid(row=0, column=0, padx=5, pady=10,  sticky="ew")

# Combobox
combobox_win = ttk.Combobox(widgets_frame, values=combo_listwin)
combobox_win.current(0)
combobox_win.grid(row=1, column=0, padx=5, pady=10,  sticky="ew")

# Combobox_d3d_DXVK_WINED3D
combobox_d3d = ttk.Combobox(widgets_frame, values=combo_listd)
combobox_d3d.current(0)
combobox_d3d.grid(row=3, column=0, padx=5, pady=10,  sticky="ew")

# Combobox_mesa
combobox_mesa = ttk.Combobox(widgets_frame, values=combo_listmes)
combobox_mesa.current(0)
combobox_mesa.grid(row=5, column=0, padx=5, pady=10,  sticky="ew")

# Combobox_builds
combobox_builds = ttk.Combobox(widgets_frame, values=combo_listbuilds)
combobox_builds.current(0)
combobox_builds.grid(row=6, column=0, padx=5, pady=10,  sticky="ew")

# Combobox_VDDX
combobox_vddx = ttk.Combobox(widgets_frame, values=combo_vddx)
combobox_vddx.current(0)
combobox_vddx.grid(row=4, column=0, padx=5, pady=10,  sticky="ew")

# Combobox_startup
combobox_startup = ttk.Combobox(widgets_frame, values=combo_startup)
combobox_startup.current(0)
combobox_startup.grid(row=7, column=0, padx=5, pady=10,  sticky="ew")

# Combobox_cores
combobox_cores = ttk.Combobox(widgets_frame, values=combo_cores)
combobox_cores.current(0)
combobox_cores.grid(row=8, column=0, padx=5, pady=10,  sticky="ew")

# Accentbutton
accentbutton = ttk.Button(widgets_frame, text="Clear", style="Accent.TButton", command=lambda: clear_button())
accentbutton.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

# Accentbutton
accentbutton = ttk.Button(widgets_frame, text="Exit", style="Accent.TButton", command=exit)
accentbutton.grid(row=10, column=0, padx=5, pady=10, sticky="nsew")

# Separator
separator = ttk.Separator(root)
separator.grid(row=10, column=0, padx=(20, 10), pady=10, sticky="ew")

separator = ttk.Separator(root)
separator.grid(row=10, column=0, padx=(20, 10), pady=10, sticky="ew", columnspan=2)

# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=12)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_1)
treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

# Treeview columns
treeview.column("#0", width=250)
treeview.column(1, anchor="w", width=120)
treeview.column(2, anchor="w", width=120)

# Pane #2
pane_2 = ttk.Frame(paned)
paned.add(pane_2, weight=3)

# Notebook
notebook = ttk.Notebook(pane_2)

# Tab #1
tab_1 = ttk.Frame(notebook)
tab_1.columnconfigure(index=0, weight=1)
tab_1.columnconfigure(index=1, weight=1)
tab_1.rowconfigure(index=0, weight=1)
tab_1.rowconfigure(index=1, weight=1)
notebook.add(tab_1, text="Adjust dxgi FPS")

# Scale
scale = ttk.Scale(tab_1, from_=100, to=0, variable=g, command=lambda event: g.set(scale.get()))
scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

# Tab #2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Progress")

# Tab #3
tab_3 = ttk.Frame(notebook)
notebook.add(tab_3, text="Warnings")

notebook.pack(expand=True, fill="both", padx=5, pady=5)

# Tab #4
tab_4 = ttk.Frame(notebook)
notebook.add(tab_4, text="Errors")

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# D3D Changing
def on_combobox_select(event):
    selected_dxvk = combobox_d3d.get()

    if selected_dxvk == "DXVK 2.3 Gpl-async":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 2.3 Gpl-async . . .")  
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk gplasync-2.3.sh"])
            treeview.insert("", "end", text="DXVK 2.3 Gpl-async Installed")
        threading.Thread(target=run_command).start()
    
    elif selected_dxvk == "DXVK 2.3":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 2.3 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk-2.3.1.sh"])
            treeview.insert("", "end", text="DXVK 2.3 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 2.2 Gpl-async":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 2.2 Gpl-async . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk gplasync-2.2.sh"])
            treeview.insert("", "end", text="DXVK 2.2 Gpl-async Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 2.2":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 2.2 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk-2.2.sh"])
            treeview.insert("", "end", text="DXVK 2.2 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 2.0 Async":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 2.0 Async . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk 2.0-async.sh"])
            treeview.insert("", "end", text="DXVK 2.0 Async Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 1.10.3 Async":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 1.10.3 Async . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk async 1.10.3.sh"])
            treeview.insert("", "end", text="DXVK 1.10.3 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK-dev":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK-dev . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk-dev.sh"])
            treeview.insert("", "end", text="DXVK-dev Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 1.6.1":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 1.6.1 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk-1.6.1.sh"])
            treeview.insert("", "end", text="DXVK 1.6.1 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 0.96":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 0.96 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk-0.96.sh"])
            treeview.insert("", "end", text="DXVK 0.96 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 2.1":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 2.1 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk-2.1.sh"])
            treeview.insert("", "end", text="DXVK 2.1 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 1.10":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 1.10 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk-1.10.sh"])
            treeview.insert("", "end", text="DXVK 1.10 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 1.10.2":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 1.10.2 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk-1.10.2.sh"])
            treeview.insert("", "end", text="DXVK 1.10.2 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 1.10.1":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 1.10.1 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk-1.10.1.sh"])
            treeview.insert("", "end", text="DXVK 1.10.1 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "DXVK 1.9.4":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing DXVK 1.9.4 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/dxvk-1.9.4.sh"])
            treeview.insert("", "end", text="DXVK 1.9.4 Installed")
        threading.Thread(target=run_command).start()
                
    elif selected_dxvk == "wined3d 8.20":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing wined3d 8.20 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/wined3d-8.20.sh"])
            treeview.insert("", "end", text="wined3d 8.20 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "wined3d 8.02":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing wined3d 8.02 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/wined3d-8.02.sh"])
            treeview.insert("", "end", text="wined3d 8.02 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "wined3d 7.21":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing wined3d 7.21 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/wined3d-7.21.sh"])
            treeview.insert("", "end", text="wined3d 7.21 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "wined3d 7.8":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing wined3d 7.8 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/wined3d-7.8.sh"])
            treeview.insert("", "end", text="wined3d 7.8 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "wined3d 7.2":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing wined3d 7.2 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/wined3d-7.2.sh"])
            treeview.insert("", "end", text="wined3d 7.2")
        threading.Thread(target=run_command).start()
        
    elif selected_dxvk == "wined3d 4.13":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing wined3d 4.13 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/d3d/wined3d-4.13sh"])
            treeview.insert("", "end", text="wined3d 4.13 Installed")
        threading.Thread(target=run_command).start()
        
# Link (Comobox_d3d)
combobox_d3d.bind("<<ComboboxSelected>>", on_combobox_select)

# Turnip Changing
def on_combobox_select(event):
    selected_mesa = combobox_mesa.get()

    if selected_mesa == "Turnip v8":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Turnip v8 . . .")  
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Turnip v8.sh"])
            treeview.insert("", "end", text="Turnip v8 Installed")
        threading.Thread(target=run_command).start()
    
    elif selected_mesa == "Turnip v7 (recommended)":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Turnip v7 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Turnip v7.sh"])
            treeview.insert("", "end", text="Turnip v7 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Turnip v6.5":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Turnip v6.5 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Turnip v6.5.sh"])
            treeview.insert("", "end", text="Turnip v6.5 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Turnip v6":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Turnip v6 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Turnip v6.sh"])
            treeview.insert("", "end", text="Turnip v6 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Turnip v5":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Turnip v5 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Turnip v5.sh"])
            treeview.insert("", "end", text="Turnip v5 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Turnip v4 (recommended)":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Turnip v4 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Turnip v4.sh"])
            treeview.insert("", "end", text="Turnip v4 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Turnip v3.5":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Turnip v3.5 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Turnip v3.5.sh"])
            treeview.insert("", "end", text="Turnip v3.5 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Turnip v3 (recommended)":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Turnip v3 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Turnip v3.sh"])
            treeview.insert("", "end", text="Turnip v3 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Turnip v2":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Turnip v2 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Turnip v2.sh"])
            treeview.insert("", "end", text="Turnip v2 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Virgl Mesa 24":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Virgl mesa 24 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Virgl 24.sh"])
            treeview.insert("", "end", text="Virgl mesa 24 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Virgl Mesa 22":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Virgl mesa 22 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Virgl 22.sh"])
            treeview.insert("", "end", text="Virgl mesa 22 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Virgl Mesa 19":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Virgl mesa 19 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Virgl 19.sh"])
            treeview.insert("", "end", text="Virgl mesa 19 Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_mesa == "Virgl 18":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Virgl mesa 18 . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/mesa/Virgl 18.sh"])
            treeview.insert("", "end", text="Virgl mesa 18 Installed")
        threading.Thread(target=run_command).start()
        
# Link (Comobox_mesa)
combobox_mesa.bind("<<ComboboxSelected>>", on_combobox_select)

# Themes
def on_combobox_select(event):
    selected_theme = combobox_win.get()

    if selected_theme == "Windows 11 Theme (Light)":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Windows 11 (Light) . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/themes/win11light.sh"])
            treeview.insert("", "end", text="Windows 11 Light Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_theme == "Windows 11 Theme (Dark)":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Windows 11 (Dark) . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/themes/win11dark.sh"])
            treeview.insert("", "end", text="Windows 11 Dark Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_theme == "Windows 10 Theme (Light)":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Windows 10 (Light) . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/themes/win10light.sh"])
            treeview.insert("", "end", text="Windows 10 Light Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_theme == "Windows 7 Theme":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Windows 7 Theme . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/themes/win7.sh"])
            treeview.insert("", "end", text="Windows 7 Theme Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_theme == "Windows XP Theme":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Windows XP Theme . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/themes/WindowsXP.sh"])
            treeview.insert("", "end", text="Windows XP Theme Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_theme == "Windows 95 Theme":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing Windows 95 Theme . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/themes/Windows95.sh"])
            treeview.insert("", "end", text="Windows 95 Theme Installed")
        threading.Thread(target=run_command).start()
        
    elif selected_theme == "MacOS Theme":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="Installing MacOS Theme . . .")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/themes/MacOS.sh"])
            treeview.insert("", "end", text="MacOS Theme Installed")
        threading.Thread(target=run_command).start()
        
# Link (Comobox_win)
combobox_win.bind("<<ComboboxSelected>>", on_combobox_select)

# Resolution
def on_combobox_select(event):
    selected_resolution = combobox_resolution.get()

    if selected_resolution == "1280x720":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="1280x720 resolution applied")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/resolution/1280x720.sh"])
        threading.Thread(target=run_command).start()
        
    elif selected_resolution == "1024x768":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="1024x768 resolution applied")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/resolution/1024x768.sh"])
        threading.Thread(target=run_command).start()
    
    elif selected_resolution == "800x600":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="800x600 resolution applied")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/resolution/800x600.sh"])
        threading.Thread(target=run_command).start()
        
    elif selected_resolution == "800x480":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="800x480 resolution applied")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/resolution/800x480.sh"])
        threading.Thread(target=run_command).start()
        
    elif selected_resolution == "640x480":
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text="640x480 resolution applied")
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/resolution/640x480.sh"])
        threading.Thread(target=run_command).start()
        
# Resolution Link
combobox_resolution.bind("<<ComboboxSelected>>", on_combobox_select)

# Define function to handle combobox selection
def on_combobox_select(event):
    selected_vddx = combobox_vddx.get()

    if selected_vddx == "VDDX 0.98":
        treeview.delete(*treeview.get_children())
        def run_command():
            subprocess.run(["python", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/vddx/vddx0.98.py"])
        threading.Thread(target=run_command).start()

    elif selected_vddx == "VDDX 1.3.2":
        treeview.delete(*treeview.get_children())
        def run_command():
            subprocess.run(["python", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/vddx/vddx1.3.2.py"])
        threading.Thread(target=run_command).start()

    elif selected_vddx == "VDDX 2.0.1":
        treeview.delete(*treeview.get_children())
        def run_command():
            subprocess.run(["python", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/vddx/vddx2.0.1.py"])
        threading.Thread(target=run_command).start()


# Link combobox_vddx to the function
combobox_vddx.bind("<<ComboboxSelected>>", on_combobox_select)

# Define function to handle combobox selection
def on_combobox_select(event):
    selected_cores = combobox_cores.get()

    if selected_cores == "2 Primary Cores":
        treeview.delete(*treeview.get_children())
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/cores/2.sh"])
        threading.Thread(target=run_command).start()

    elif selected_cores == "3 Primary Cores":
        treeview.delete(*treeview.get_children())
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/cores/3.sh"])
        threading.Thread(target=run_command).start()

    elif selected_cores == "4 Primary Cores":
        treeview.delete(*treeview.get_children())
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/cores/4.sh"])
        threading.Thread(target=run_command).start()
        
    elif selected_cores == "5 Primary Cores":
        treeview.delete(*treeview.get_children())
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/cores/5.sh"])
        threading.Thread(target=run_command).start()

    elif selected_cores == "6 Primary Cores":
        treeview.delete(*treeview.get_children())
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/cores/6.sh"])
        threading.Thread(target=run_command).start()
        
    elif selected_cores == "7 Primary Cores":
        treeview.delete(*treeview.get_children())
        def run_command():
            subprocess.run(["bash", "/data/data/com.termux/files/usr/glibc/opt/libs/scripts/cores/6.sh"])
        threading.Thread(target=run_command).start()


# Link combobox_vddx to the function
combobox_cores.bind("<<ComboboxSelected>>", on_combobox_select)

# Window Size
root.geometry("1170x625")

# Start the main loop
root.mainloop()