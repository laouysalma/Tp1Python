from datetime import datetime
class Article:
    def __init__(self,reference:str,designation: str ,prix_ht: float,stock: int):
       self.reference=reference
       self.designation=designation
       self.prix_ht=prix_ht
       self.stock=stock


    def valeur_stock(self) -> float:
        return self.prix_ht * self.stock 
    
    def __str__(self):
      return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht} € HT"  
    
    def valeur_stock(self):
        return self.prix_ht * self.stock
    
    def approvisionner(self, qte: int):
        if qte <= 0:
            raise ValueError("La quantité doit être positive.")

        self.stock += qte

        with open("mouvements.log", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} — Article {self.reference} : +{qte} unités (nouveau stock = {self.stock})\n")