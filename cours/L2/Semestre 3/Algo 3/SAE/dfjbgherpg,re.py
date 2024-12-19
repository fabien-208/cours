import csv
from tkinter import messagebox

def load_date(file_path, required_columns):

    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Valider les colonnes
            missing_columns = [col for col in required_columns if col not in reader.fieldnames]
            if missing_columns:
                raise ValueError(f"Colonnes manquantes: {', '.join(missing_columns)}")

            # Charger les données
            data = []
            for row in reader:
                if any(value.strip() == '' for value in row.values()):
                    raise ValueError("Le fichier contient des valeurs manquantes.")
                data.append(row)

            return data

    except FileNotFoundError:
        messagebox.showerror("Erreur", "Le fichier CSV n'a pas été trouvé.")
    except ValueError as ve:
        messagebox.showerror("Erreur de validation", str(ve))
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur inattendue s'est produite: {str(e)}")

    return None

# Exemple d'utilisation dans une application Tkinter
if __name__ == "__main__":
    import tkinter as tk
    from tkinter.filedialog import askopenfilename

    def charger_fichier():
        file_path = askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
        if file_path:
            required_columns = ["ID", "Revenu (\u20ac) Mensuel", "Montant du Pr\u00eat (\u20ac)", "Durée de l’Emploi (années)", "Historique de Crédit", "Prêt Approuvé"]
            data = load_date(file_path, required_columns)
            if data:
                messagebox.showinfo("Succès", "Fichier chargé et validé avec succès.")

    # Interface Tkinter
    root = tk.Tk()
    root.title("Validation de fichier CSV")

    charger_btn = tk.Button(root, text="Charger un fichier CSV", command=charger_fichier)
    charger_btn.pack(pady=20)

    root.mainloop()
