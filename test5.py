from convertisseur import Convertisseur

montant = 100
print("Conversion en dh avant mise à jour :", Convertisseur.vers_dh(montant))
print("Conversion en euro avant mise à jour ",Convertisseur.vers_eur(montant))
Convertisseur.mettre_a_jour_taux(11.2)
print("Conversion en dh après mise à jour  :", Convertisseur.vers_dh(montant))
print("Conversion en euro après mise à jour ",Convertisseur.vers_eur(montant))