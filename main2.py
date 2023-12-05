import tkinter as tk

#garde en mémoire la valeur affiché dans l'entry
def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

#calcule le résultat
def calculate():
    """hop"""
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
        entry.config(bg='lightgreen')  # Fond vert si le calcul réussit
    except Exception:
        entry_var.set("Error")
        entry.config(bg='lightcoral')  # Fond rouge en cas d'erreur

#efface ce l'entry
def clear_entry():
    entry_var.set("")
    entry.config(bg='white') #fond blanc lors du clear

def change_color(x):
    button.config(bg='black')  # Changer la couleur du bouton lorsqu'il est cliqué
    window.after(75, lambda: button.config(bg='lightgray'))  # Revenir à la couleur d'origine après un court délai

# Création de la fenêtre principale
window = tk.Tk()
window.title("Calculatrice")
window.configure(bg='linen')  # Changer la couleur du fond

# Variable pour stocker le texte de l'entry
entry_var = tk.StringVar()

# Entry pour afficher les chiffres et les résultats
entry = tk.Entry(window, textvariable=entry_var, justify="right", font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)


# Boutons pour les chiffres de 1 à 9
for i in range(1, 10):
    row_val = (i - 1) // 3 + 1
    col_val = (i - 1) % 3
    tk.Button(window, text=str(i), command=lambda i=i: on_button_click(i), font=('Arial', 14), bg='lightgray', width=5, height=2).grid(row=row_val, column=col_val)
button = tk.Button(window, text=str(0), command=lambda x=0: [on_button_click(x), change_color(button)], font=('Arial', 14), bg='lightgray', width=5, height=2)
button.grid(row=4, column=1)
# Boutons pour les opérations +, -, *, /
tk.Button(window, text='+', command=lambda op='+': on_button_click(op), font=('Arial', 14), bg='lightblue', width=5, height=2).grid(row=1, column=3)
tk.Button(window, text='-', command=lambda op='-': on_button_click(op), font=('Arial', 14), bg='lightblue', width=5, height=2).grid(row=1, column=4)
tk.Button(window, text='*', command=lambda op='*': on_button_click(op), font=('Arial', 14), bg='lightblue', width=5, height=2).grid(row=2, column=3)
tk.Button(window, text='/', command=lambda op='/': on_button_click(op), font=('Arial', 14), bg='lightblue', width=5, height=2).grid(row=2, column=4)

# Bouton égal
tk.Button(window, text='=', command=calculate, font=('Arial', 14), bg='mediumturquoise', width=5, height=2).grid(row=3, column=3)

# Bouton C (Clear)
tk.Button(window, text='C', command=clear_entry, font=('Arial', 14), bg='mediumturquoise', width=5, height=2).grid(row=3, column=4)

# Lancement de la boucle principale
window.mainloop()