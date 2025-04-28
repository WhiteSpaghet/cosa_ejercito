import tkinter as tk
from logica_lineal.optimizador import optimize_army

def run_app():
    def solve():
        result = optimize_army()
        result_text.set(f"💪 Power Total: {result['total_power']}\n\n"
                        f"🗡️ Espadachines: {result['swordsmen']}\n"
                        f"🏹 Arqueros: {result['bowmen']}\n"
                        f"🐎 Jinetes: {result['horsemen']}")

    root = tk.Tk()
    root.title("Optimizador de Ejército")

    tk.Label(root, text="Presiona para optimizar el ejército").pack(pady=10)
    tk.Button(root, text="Optimizar", command=solve).pack(pady=5)

    result_text = tk.StringVar()
    tk.Label(root, textvariable=result_text, justify="left").pack(padx=10, pady=10)

    root.mainloop()