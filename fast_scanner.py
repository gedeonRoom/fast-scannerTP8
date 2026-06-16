import socket
import threading
from queue import Queue
from datetime import datetime

# ==========================================
# 1. CONFIGURATION
# ==========================================
cible = "127.0.0.1"
file_attente = Queue()
verrou_affichage = threading.Lock()  # Notre synchronisation pour un affichage propre
ports_ouverts = []

# ==========================================
# 2. LA FONCTION DU WORKER (Le travailleur)
# ==========================================
def scan_port():
    while not file_attente.empty():
        # Le thread récupère le prochain port dans la file
        port = file_attente.get()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            resultat = sock.connect_ex((cible, port))

            if resultat == 0:
                # On verrouille l'écran juste le temps d'afficher le message
                with verrou_affichage:
                    print(f"[+] Le port {port} est OUVERT")
                ports_ouverts.append(port)
            sock.close()
        except:
            pass
        finally:
            # Le thread signale qu'il a fini sa tâche
            file_attente.task_done()

# ==========================================
# 3. INITIALISATION ET LANCEMENT
# ==========================================
if __name__ == "__main__":
    print("-" * 50)
    print(f"[*] Scan multithreadé de la cible : {cible}")
    heure_debut = datetime.now()
    print(f"[*] Heure de début : {heure_debut}")
    print("-" * 50)

    # On remplit la file d'attente avec les ports (ex: 20 à 1024)
    for port in range(20, 1025):
        file_attente.put(port)

    # On crée et on lance 10 threads simultanés
    for _ in range(10):
        thread = threading.Thread(target=scan_port)
        # daemon=True permet aux threads de s'arrêter si le programme principal s'arrête
        thread.daemon = True
        thread.start()

    # On demande au programme principal d'attendre que la file soit vide
    file_attente.join()

    heure_fin = datetime.now()
    temps_total = heure_fin - heure_debut

    print("-" * 50)
    print(f"[*] Scan terminé en {temps_total}")
    print(f"[*] Total des ports ouverts trouvés : {len(ports_ouverts)}")
