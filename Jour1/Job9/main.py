
#Job 9
nom = "Smartphone"
prix_unitaire = 500
quantite_en_stock = 120
print("Informations sur le produit initiales :")
print("Nom du produit :", nom)
print(f"Prix unitaire : {prix_unitaire} €")
print("Quantité en stock :",quantite_en_stock)
quantite_ajoutee = int(input("Combien de produits souhaitez-vous ajouter au stock ? : "))
quantite_en_stock += quantite_ajoutee

print(f"{quantite_ajoutee}, produit(s) ajouté(s) au stock.")
quantite_achetee = int(input("Combien de produits souhaitez-vous acheter ? "))

if quantite_achetee <= quantite_en_stock:
    quantite_en_stock -= quantite_achetee
    total_achat = quantite_achetee * prix_unitaire
    print(f"Achat effectué : {quantite_achetee} produit(s) acheté(s) pour {total_achat}€.")
else:
    print("Désolé, il n'y a pas suffisamment de stock.")

print(f"Quantité restante en stock : {quantite_en_stock}")
prix_unitaire *= 1.10
print("\nInformations après l'inflation :")
print(f"Nom du produit : {nom}")
print(f"Prix unitaire après inflation : {prix_unitaire:.2f}€")
print(f"Quantité en stock : {quantite_en_stock}")
