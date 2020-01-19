"""
Ferriere Tom
2°9
"""

from math import sqrt

xA=int(input("[>] Donner l'abscisse de A: "))
yA=int(input("[>] Donner l'ordonnée de A: "))

xB=int(input("\n[>] Donner l'abscisse de B: "))
yB=int(input("[>] Donner l'ordonnée de B: "))

xC=int(input("\n[>] Donner l'abscisse de C: "))
yC=int(input("[>] Donner l'ordonnée de C: "))

print(f"\n[<] Le vecteur AB a pour coordonnées ({(xB-xA)}, {(yB-yA)})")
print(f"[<] Le vecteur AC a pour coordonnées ({(xC-xA)}, {(yC-yA)})")
print(f"[<] Le vecteur BC a pour coordonnées ({(xC-xB)}, {(yC-yB)})")

AB=(xB-xA)**2+(yB-yA)**2
AC=(xC-xA)**2+(yC-yA)**2
BC=(xC-xB)**2+(yC-yB)**2

print(f"\n[<] Le segment [AB] a approximativement pour longueur {sqrt(AB)}cm")
print(f"[<] Le segment [AC] a approximativement pour longueur {sqrt(AC)}cm")
print(f"[<] Le segment [BC] a approximativement pour longueur {sqrt(BC)}cm")

if BC==AB+AC:
	print("\n[!] Le triangle ABC est rectangle en A")
	print(f"[<] Le centre du cercle circonscrit est J({(xB+xC)/2}, {(yB+yC)/2}) et le rayon BC/2 vaut approximativement {sqrt(BC)/2}cm")
elif AC==AB+BC:
	print("\n[!] Le triangle ABC est rectangle en B")
	print(f"[<] Le centre du cercle circonscrit est J({(xA+xC)/2}, {(yA+yC)/2}) et le rayon AC/2 vaut approximativement {sqrt(AC)/2}cm")
elif AB==AC+BC:
	print("\n[!] Le triangle ABC est rectangle en C")
	print(f"[<] Le centre du cercle circonscrit est J({(xA+xB)/2}, {(yA+yB)/2}) et le rayon AB/2 vaut approximativement {sqrt(AB)/2}cm")
else:
	print("\n[!] Le triangle ABC n'est pas rectangle.")