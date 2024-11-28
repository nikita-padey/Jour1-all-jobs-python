#Job 4
#print("abcdefghijklmnopqrstuvwxyz")

#Job 5
#print("zyxwvutsrqponmlkjihgfedcba")

#Job 6
#ma_string = "Je suis une String"
#print(ma_string)

#Job 7
#num1 = 40
#num2 = 2
#print(num1 + num2)

#Job 8
#num1 = 3
#num2 = 14
#print(num1 * num2)


#Job 9
#nom = "Smartphone"
#prix_unitaire = 500
#quantite_en_stock = 120
#print("Informations sur le produit initiales :")
#print("Nom du produit :", nom)
#print(f"Prix unitaire : {prix_unitaire} €")
#print("Quantité en stock :",quantite_en_stock)
#quantite_ajoutee = int(input("Combien de produits souhaitez-vous ajouter au stock ? : "))
#quantite_en_stock += quantite_ajoutee
#print(f"{quantite_ajoutee}, produit(s) ajouté(s) au stock.")
#quantite_achetee = int(input("Combien de produits souhaitez-vous acheter ? "))
#if quantite_achetee <= quantite_en_stock:
#    quantite_en_stock -= quantite_achetee
#    total_achat = quantite_achetee * prix_unitaire
#    print(f"Achat effectué : {quantite_achetee} produit(s) acheté(s) pour {total_achat}€.")
#else:
#    print("Désolé, il n'y a pas suffisamment de stock.")
#print(f"Quantité restante en stock : {quantite_en_stock}")
#prix_unitaire *= 1.10
#print("\nInformations après l'inflation :")
#print(f"Nom du produit : {nom}")
#print(f"Prix unitaire après inflation : {prix_unitaire:.2f}€")
#print(f"Quantité en stock : {quantite_en_stock}")

#Job 10

montant_investissement = int(input("C'est quoi ta maxi moula : "))
taux_rendement = 5

gain_annuel_initial = montant_investissement * (taux_rendement / 100)
print(f"Gain annuel initial : {gain_annuel_initial:.2f} euros")

montant_investissement += 5000
taux_rendement += 2

gain_annuel_apres_ajout = montant_investissement * (taux_rendement / 100)
print(f"\nAprès ajout de 5000€, nouveau montant : {montant_investissement}€")
print(f"Nouveau taux de rendement : {taux_rendement}%")
print(f"Gain annuel après ajout : {gain_annuel_apres_ajout} euros")

montant_investissement -= montant_investissement * 0.10
taux_rendement -= 1

gain_annuel_apres_retrait = montant_investissement * (taux_rendement / 100)
print(f"\nAprès retrait de 10%, nouveau montant : {montant_investissement:.2f}€")
print(f"Nouveau taux de rendement après retrait : {taux_rendement}%")
print(f"Gain annuel après retrait : {gain_annuel_apres_retrait:.2f} euros")



