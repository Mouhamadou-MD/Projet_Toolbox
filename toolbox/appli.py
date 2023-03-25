import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import nmap
import datetime
import subprocess
import theHarvester
import sherlock
#APPLI.PY

# Créer la fenêtre principale
root = tk.Tk()
root.title("Ma toolbox---Mouhamadou_Diallo copyright2023")

# Définir une fonction pour ouvrir un fichier
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)

# Définir une fonction pour lancer un scan rapide
def scan_hosts():
    host = tk.simpledialog.askstring("Hôte à scanner", "Entrez l'adresse IP de l'hôte ou du réseau à scanner:")
    file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") +"-Fast_Nmap"+ ".txt"
    with open(file_name, "w") as f:
        subprocess.run(["nmap", "-Pn", host], stdout=f)
    tk.messagebox.showinfo("Scan terminé", f"Le scan de {host} est terminé. Les résultats ont été enregistrés dans le fichier {file_name}.")
        
# Définir une fonction pour lancer un scan précis
def scan_hosts_slow():
    host = tk.simpledialog.askstring("Hôte à scanner", "Entrez l'adresse IP de l'hôte ou du réseau à scanner:")
    file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") +"-Slow_Nmap"+ ".txt"
    with open(file_name, "w") as f:
        subprocess.run(["nmap", "-Pn", host], stdout=f)
    tk.messagebox.showinfo("Scan terminé", f"Le scan de {host} est terminé. Les résultats ont été enregistrés dans le fichier {file_name}.")

# Définir une fonction pour lancer un scan de vulnérabilité
def scan_vuln():
	host = tk.simpledialog.askstring("Hôte à scanner", "Entrez l'adresse IP de l'hôte ou du réseau à scanner:")
	file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") +"-Vuln_Nmap"+ ".txt"
	with open(file_name, "w") as f:
		#mis à jour de la base de donneés + Lancement du scan 
		cmd= f"sudo nmap --script-updatedb && nmap -Pn -sV --script vuln {host}>{file_name}"
		subprocess.run(cmd, shell=True)
	tk.messagebox.showinfo("Scan terminé", f"Le scan de {host} est terminé. Les résultats ont été enregistrés dans le fichier {file_name}.")
	
	

# Définir une fonction pour lancer TheHarvester
def run_theHarvester(mode):
    domain = tk.simpledialog.askstring("Domaine à scanner", "Entrez le nom de domaine à scanner:")
    if domain:
        file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") +"theHarverster"+ ".txt"
        if mode == "emails":
            cmd = f"theHarvester -d {domain}  -b all > {file_name}"
        elif mode == "hosts":
            cmd = f"theHarvester -d {domain}  -b all > {file_name}"
        elif mode == "all":
            cmd = f"theHarvester -d {domain}  -b all > {file_name}"
        subprocess.run(cmd, shell=True)
        tk.messagebox.showinfo("Scan terminé", f"Le scan de {domain} est terminé. Les résultats ont été enregistrés dans le fichier {file_name}.")
        
        
# Définir une fonction pour lancer Sherlock
def scan_username():
    # Demander à l'utilisateur d'entrer un nom d'utilisateur
    nom_user = tk.simpledialog.askstring("Nom d'utilisateur à scanner", "Entrez le nom d'utilisateur à scanner:")
    if nom_user != "":
    	file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") +"user_scan"+ ".txt"

    # Exécuter la commande sherlock pour rechercher les informations
    	command = f"sherlock  --timeout 1 {nom_user} > {file_name}"
    	subprocess.run(command, shell=True)
    	tk.messagebox.showinfo("Scan terminé", f"Le scan de {nom_user} est terminé. Les résultats ont été enregistrés dans le fichier {file_name}.")
        

# Créer une barre de menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Ouvrir", command=open_file)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Créer un menu pour Nmap
nmap_menu = tk.Menu(menu_bar, tearoff=0)
nmap_menu.add_command(label="Scan rapide", command=scan_hosts)
nmap_menu.add_command(label="Scan complet", command=scan_hosts_slow)
nmap_menu.add_command(label="Scan de vulnerabilité", command=scan_vuln)
menu_bar.add_cascade(label="Nmap", menu=nmap_menu)

# Créer un menu pour theHarvester
theharvester_menu = tk.Menu(menu_bar, tearoff=0)
#theharvester_menu.add_command(label="Search emails", command=lambda: run_theHarvester("emails"))
#theharvester_menu.add_command(label="Search hosts", command=lambda: run_theHarvester("hosts"))
theharvester_menu.add_command(label="recherche d'informations sur un nom de domaine", command=lambda: run_theHarvester("all"))
menu_bar.add_cascade(label="theHarvester", menu=theharvester_menu)

# Créer un menu pour Sherlock
sherlock_menu = tk.Menu(menu_bar, tearoff=0)
sherlock_menu.add_command(label="Rechercher des noms d'utilisateurs sur les réseaux sociaux", command=scan_username)
menu_bar.add_cascade(label="Sherlock", menu=sherlock_menu)



root.config(menu=menu_bar)



# Créer une zone de texte pour le code
text_area = tk.Text(root, font=("Helvetica", 12))
text_area.pack(fill=tk.BOTH, expand=True)

# Lancer la boucle principale de l'application
root.mainloop()
