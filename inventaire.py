from article import Article

ar1=Article("ref1","dest1",12.5,3)
ar2=Article("ref2","dest2",150.5,1)
ar3=Article("ref3","dest3",65.25,2)

print(ar1)
print(ar2)
print(ar3)

ar1.approvisionner(5)
print("approvisionnement",ar1)

articles =[ar1,ar2,ar3]
total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d’inventaire : {total:.2f} €")