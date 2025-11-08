from carnet import Carnet
from contact import Contact

carn = Carnet()
carn.ajouter(Contact("khadija laamiri", "0600110033", "laamiri@example.com"))
carn.ajouter(Contact("enami fatima-ezzahra", "0600000000", "ennami@example.com"))
carn.ajouter(Contact("laouy fouad", "0744552288", "laouy@example.com"))

resultat = carn.recherche("la")
for contact in resultat:
    print(contact.nom, contact.telephone)

print("Nombre total de contacts :", carn.nbr_contacts)
