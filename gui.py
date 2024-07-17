import tkinter as tk
from tkinter import ttk
from main import *

root = tk.Tk()
root.geometry('710x600')
root.title('XDefiant KD Recorder')

root.option_add("*tearOff", False)
root.resizable(False, False)
root.iconbitmap('assets/icon.ico')

style = ttk.Style(root)
root.tk.call('source', 'assets/forest-dark.tcl')
style.theme_use("forest-dark")

# Set the default value of the variable 
k = tk.StringVar(root)
k.set(0)
d = tk.StringVar(root)
d.set(0)
options_list = ["Choose Gamemode", "Escort", "Zone Control", "Domination", "Occupy", "Hot Shot", "CTF", "TDM"]
value_inside = tk.StringVar(root) 
value_inside.set("Select an Option")

# Create a Frame for add KD
kd_frame = ttk.LabelFrame(root, text="Add KD", padding=(20, 10))
kd_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# Add KD
glabel = ttk.Label(kd_frame, text='Gamemode', font='Arial 10', justify='center')
glabel.grid(row=0, column=0, padx=10)
option = ttk.OptionMenu(kd_frame, value_inside, *options_list)
option.config(width=20)
option.grid(row=1, column=0, padx=5, pady=10, sticky='ew')

klabel = ttk.Label(kd_frame, text='Kills', font='Arial 10', justify='center')
klabel.grid(row=0, column=1, padx=10)
kills = ttk.Spinbox(kd_frame, from_=0, to=999, textvariable=k)
kills.grid(row=1, column=1, padx=10)

dlabel = ttk.Label(kd_frame, text='Deaths', font='Arial 10', justify='center')
dlabel.grid(row=0, column=2, padx=10)
deaths = ttk.Spinbox(kd_frame, from_=0, to=999, textvariable=d)
deaths.grid(row=1, column=2, padx=10)

button = ttk.Button(kd_frame, text='Add Record', style="Accent.TButton", command=lambda: new_kd(value_inside.get(), float(k.get()), float(d.get())))
button.grid(row=2, column=0, columnspan=3, pady=10, padx=5, sticky='ew')
reset = ttk.Button(kd_frame, text='Reset', command=resetDB)
reset.grid(row=3, column=0, columnspan=3, pady=10, padx=5, sticky='ew')

# KD Show Frame
kds_frame = ttk.LabelFrame(root, text="Your KDs", padding=(20, 10))
kds_frame.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# Add Info
info0 = get_gamemode_info(gamemodes[0])
kdmode_label_0 = ttk.Label(kds_frame, text=f'{gamemodes[0]}', font='Arial 10', justify='center')
kdmode_label_0.grid(row=0, column=0, padx=(110, 10), pady=(2, 2))
kdmode_labelI_0 = ttk.Label(kds_frame, text=f'{info0['kd']} KDR', font='Arial 10', justify='center')
kdmode_labelI_0.grid(row=1, column=0, padx=(110, 10), pady=(2, 20))

info1 = get_gamemode_info(gamemodes[1])
kdmode_label_1 = ttk.Label(kds_frame, text=f'{gamemodes[1]}', font='Arial 10', justify='center')
kdmode_label_1.grid(row=0, column=1, padx=(110, 10), pady=(2, 2))
kdmode_labelI_1 = ttk.Label(kds_frame, text=f'{info1['kd']} KDR', font='Arial 10', justify='center')
kdmode_labelI_1.grid(row=1, column=1, padx=(110, 10), pady=(2, 20))

info2 = get_gamemode_info(gamemodes[2])
kdmode_label_2 = ttk.Label(kds_frame, text=f'{gamemodes[2]}', font='Arial 10', justify='center')
kdmode_label_2.grid(row=0, column=2, padx=(110, 10), pady=(2, 2))
kdmode_labelI_2 = ttk.Label(kds_frame, text=f'{info2['kd']} KDR', font='Arial 10', justify='center')
kdmode_labelI_2.grid(row=1, column=2, padx=(110, 10), pady=(2, 20))

info3 = get_gamemode_info(gamemodes[3])
kdmode_label_3 = ttk.Label(kds_frame, text=f'{gamemodes[3]}', font='Arial 10', justify='center')
kdmode_label_3.grid(row=2, column=0, padx=(110, 10), pady=(2, 2))
kdmode_labelI_3 = ttk.Label(kds_frame, text=f'{info3['kd']} KDR', font='Arial 10', justify='center')
kdmode_labelI_3.grid(row=3, column=0, padx=(110, 10), pady=(2, 20))

info4 = get_gamemode_info(gamemodes[4])
kdmode_label_4 = ttk.Label(kds_frame, text=f'{gamemodes[4]}', font='Arial 10', justify='center')
kdmode_label_4.grid(row=2, column=1, padx=(110, 10), pady=(2, 2))
kdmode_labelI_4 = ttk.Label(kds_frame, text=f'{info4['kd']} KDR', font='Arial 10', justify='center')
kdmode_labelI_4.grid(row=3, column=1, padx=(110, 10), pady=(2, 20))

info5 = get_gamemode_info(gamemodes[5])
kdmode_label_5 = ttk.Label(kds_frame, text=f'{gamemodes[5]}', font='Arial 10', justify='center')
kdmode_label_5.grid(row=2, column=2, padx=(110, 10), pady=(2, 2))
kdmode_labelI_5 = ttk.Label(kds_frame, text=f'{info5['kd']} KDR', font='Arial 10', justify='center')
kdmode_labelI_5.grid(row=3, column=2, padx=(110, 10), pady=(2, 20))

info6 = get_gamemode_info(gamemodes[6])
kdmode_label_6 = ttk.Label(kds_frame, text=f'{gamemodes[6]}', font='Arial 10', justify='center')
kdmode_label_6.grid(row=4, column=1, padx=(110, 10), pady=(2, 2))
kdmode_labelI_6 = ttk.Label(kds_frame, text=f'{info6['kd']} KDR', font='Arial 10', justify='center')
kdmode_labelI_6.grid(row=5, column=1, padx=(110, 10), pady=(2, 20))

def refresh():
    kdmode_labelI_0.config(text=f'{info0['kd']} KDR')
    kdmode_labelI_1.config(text=f'{info1['kd']} KDR')
    kdmode_labelI_2.config(text=f'{info2['kd']} KDR')
    kdmode_labelI_3.config(text=f'{info3['kd']} KDR')
    kdmode_labelI_4.config(text=f'{info4['kd']} KDR')
    kdmode_labelI_5.config(text=f'{info5['kd']} KDR')
    kdmode_labelI_6.config(text=f'{info6['kd']} KDR')

refresh = ttk.Button(kds_frame, text='Refresh', style="Accent.TButton", command=refresh)
refresh.grid(row=6, column=0, columnspan=6, pady=10, padx=(75, 10), sticky='ew')

sign = ttk.Label(root, text='Made by weed.Tomii | Discord @gtomii_', font='Courier  10')
sign.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()