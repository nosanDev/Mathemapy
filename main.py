# main.py
from src.pythagore import Pythagore
from src.graphique import Graphique
from src.thales import Thales

def main() :
  print("""  __  __    _  _____ _   _ _____ __  __    _    ______   __
 |  \/  |  / \|_   _| | | | ____|  \/  |  / \  |  _ \ \ / /
 | |\/| | / _ \ | | | |_| |  _| | |\/| | / _ \ | |_) \ V / 
 | |  | |/ ___ \| | |  _  | |___| |  | |/ ___ \|  __/ | |  
 |_|  |_/_/   \_\_| |_| |_|_____|_|  |_/_/   \_\_|    |_|  
                                                           """)

  print("""Ce programme polyvalent permet différent calcul, veuillez choisir en renseignant le numéro correspondant à la fonction voulue. :
  \n - 1 : Pythagore
  \n - 2 : Graphique
  \n - 3 : Thalès""")

  choix = int(input("\nVotre choix : "))
  
  
  if choix == 1 :
    Pythagore()

  if choix == 2 :
    Graphique()

  if choix == 3 :
    Thales()
      
      


if __name__ == "__main__":
    main()
    m = float(input("Entrez la pente (m) de la fonction affine : "))
    c = float(input("Entrez la constante (c) de la fonction affine : "))
    Graphique(m, c)