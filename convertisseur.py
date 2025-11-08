class Convertisseur:
    taux_eur_dh = 10.9
    @staticmethod
    def vers_dh(euros: float) -> float:
        return euros * Convertisseur.taux_eur_dh
    @staticmethod
    def vers_eur(dhs: float) -> float:
        return dhs / Convertisseur.taux_eur_dh

    @classmethod
    def mettre_a_jour_taux(cls, nv_taux: float):
        cls.taux_eur_dh= nv_taux
    
