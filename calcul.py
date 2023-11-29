run = True

def addition (x, y):
    return  float(x) + float(y)

def soustraction(x, y):
    return float(x) - float(y)

def multiplication (x, y):
    return float(x) * float(y)

def division (x , y):
    if y != 0:
        return float(x) / float(y)
    else:
        return "Erreur: Division par zéro"

def puissance(x, y):
    return float(x)**float(y)

def calcul(opérateur,nombre1,nombre2):
    global run
    try:
        if opérateur == "+":
            resultat = addition(nombre1,nombre2)

        elif opérateur == "-":
            resultat = soustraction(nombre1,nombre2)

        elif opérateur == "*":
            resultat = multiplication(nombre1,nombre2)

        elif opérateur == "/":
            resultat = division(nombre1,nombre2)

        elif opérateur == "**":
            resultat = puissance(nombre1,nombre2)

        else:
            print("Choix invalide. Veuillez choisir un autre opérateur")
            run = False
    except ValueError:
        print("Veuillez entrez des chiffres valides")

    return resultat

def quitter(x):
    if x == "q".lower():
        while True:
            reponse = input("Voulez-vous quitter ? (y/n): ").lower()
            if reponse == 'y':
                print("Au revoir!")
                exit()
            elif reponse == 'n':
                print("Continuons...")
                calculatrice()
            else:
                print("Réponse non valide. Veuillez entrer 'y' pour oui ou 'n' pour non.")
    else:
        return


def calculatrice():
    historique = []
    liste = ""
    resultat = ""
    nombre1 = ""
    nombre2 = ""
    opérateur = ""
    global run
    while run:
  

        #demander à l'utilisateur de rentrer deux nombres
        if resultat == "":

            nombre1 = input("Entrez un chiffre : ")
            quitter(nombre1)
            opérateur = input("entrez l'opérateur : ")
            quitter(opérateur)
            nombre2 = input("Entrez un chiffre : ")
            quitter(nombre2)
            liste = str(nombre1) + str(opérateur) + str(nombre2)
            historique.append(liste)
            resultat=calcul(opérateur,nombre1,nombre2)

        elif resultat != "":
            try:
                historique[0] = liste
                nombre1 = resultat
                print("historique :", historique)
                print("total :",resultat)
                opérateur = input("entrez l'opérateur : ")
                quitter(opérateur)
                nombre2 =  float(input("Entrez un chiffre : "))
                quitter(nombre2)
                liste +=str(opérateur) + str(nombre2) 

            except ValueError:
                print("Veuillez entrez des chiffres valides")
            resultat=calcul(opérateur,nombre1,nombre2)
        continue




calculatrice()