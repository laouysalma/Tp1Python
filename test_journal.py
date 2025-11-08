from journal import JournalTaches
from time import sleep

with JournalTaches() as journal:
    journal.enregistrer("raliser les tps de java ")
    sleep(1)
    journal.enregistrer("voir la suite de course python sur youtube")
    sleep(1)
    journal.enregistrer("reviser le module de didactique")

print("l’historique dans l’ordre chronologique invers")
JournalTaches.lire()
