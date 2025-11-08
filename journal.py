from datetime import datetime

class JournalTaches:
    def __enter__(self):
        self._fichier = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        horodatage = datetime.now().isoformat()
        self._fichier.write(f"{horodatage} — {tache}\n")

    def __exit__(self, exc_type, exc, tb):
        self._fichier.close()

    @classmethod
    def lire(cls):
        try:
            with open("journal.txt", "r", encoding="utf-8") as f:
                lignes = f.readlines()
            for ligne in reversed(lignes):
                print(ligne.strip())
        except FileNotFoundError:
            print("Aucun journal trouvé.")
