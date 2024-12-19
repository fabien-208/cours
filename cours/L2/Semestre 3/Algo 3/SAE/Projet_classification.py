import tkinter as tk
from tkinter import ttk

fenetre = tk.Tk()
fenetre.title("Choix d'algorithme de classification")

load_button = tk.Button(fenetre, text="Charger données", command=ctrl.load_data)
load_button.pack(pady=10)

file_status_label = tk.Label(fenetre, text="Aucun fichier chargé")
file_status_label.pack(pady=5)

algorithm_var = tk.StringVar(value="CART")
algorithm_menu = ttk.Combobox(fenetre, textvariable=algorithm_var)
algorithm_menu['values'] = ("CART", "RF")
algorithm_menu.pack(pady=5)

run_button = tk.Button(fenetre, text="Lancer")
run_button.pack(pady=10)

fenetre.mainloop()
