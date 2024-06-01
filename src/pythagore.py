import math

def Pythagore() :
  print("""\n Ce programme permet de calculer la longueur d'un côté d'un triangle rectangle. \n \n Merci de rentrer les valeurs des deux autres côtés. (0 pour ceux dont vous la longueur dont vous chercher la valeur. """)
  
  AB = float(input("AB = "))
  BC = float(input("BC = "))
  AC = float(input("AC = "))

  if AB == 0 :
    V = math.sqrt(BC**2 + AC**2)
    print("AB = ", AB)
  else :
    if BC == 0 :
      V = math.sqrt(AB**2 - AC**2)
      print("BC = ", BC)
    else :
      if AC == 0 :
        V = math.sqrt(AB**2 - BC**2)
        print("AC = ", AC)
      else :
        print("Vous avez rentré une valeur incorrecte.")

  print("La longueur manquante à pour valeur" + V)