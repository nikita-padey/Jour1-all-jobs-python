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



