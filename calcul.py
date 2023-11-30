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


    if opérateur == "+":
        resultat = addition(nombre1,nombre2)

    elif opérateur == "-":
        resultat = soustraction(nombre1,nombre2)

    elif opérateur == "*" or opérateur == "x":
        resultat = multiplication(nombre1,nombre2)

    elif opérateur == "/":
        resultat = division(nombre1,nombre2)

    elif opérateur == "**":
        resultat = puissance(nombre1,nombre2)

    return resultat

def est_operateur(val):
    operateurs_valides = ['+', '-', '*', '/', '**']

    return val in operateurs_valides

def quitter(x):
    if x == "q":
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

    def clear_variables(x):
        nonlocal historique, liste, resultat, nombre1, nombre2, opérateur
        if x =="c":
            if historique == []:
                print ("pas d'historique")
            else:
                print(f"{historique[0]}={resultat}")
                print("Nouveau calcul :")
            historique.clear()
            liste = ""
            resultat = ""
            nombre1 = ""
            nombre2 = ""
            opérateur = ""

        else:
            return


    while True:

        run = True
        while run:
            #demander à l'utilisateur de rentrer deux nombres
            if resultat == "":

                nombre1 = input("Entrez un chiffre : ").lower()
                if nombre1.isalpha() or est_operateur(nombre1):

                    if nombre1 != "q" and nombre1 !="c":

                        print("Veuillez entrez des chiffres valides")
                        run = False
                    else:

                        clear_variables(nombre1)
                        quitter(nombre1)
                        run = False
                else:

                    opérateur = input("entrez l'opérateur : ").lower()
                    if opérateur.isalpha():

                        if opérateur != "q" and opérateur !="c":

                            print("Veuillez entrez des chiffres valides")
                            run = False
                        else:

                            clear_variables(opérateur)
                            quitter(opérateur)
                            run = False
                    elif est_operateur(opérateur):
                        print(f"{opérateur} est un opérateur valide.")

                        nombre2 = input("Entrez un chiffre : ").lower()
                        if nombre2.isalpha() or est_operateur(nombre2):

                            if nombre2 != "q" and nombre2 !="c":

                                print("Veuillez entrez des chiffres valides")
                                run = False
                            else:

                                clear_variables(nombre2)
                                quitter(nombre2)
                                run = False
                        else:

                            liste = str(nombre1) + str(opérateur) + str(nombre2)
                            historique.append(liste)
                            resultat=calcul(opérateur,nombre1,nombre2)
                    else:
                        print(f"{opérateur} n'est pas un opérateur valide.")
                        run = False

            elif resultat != "":
                
                historique[0] = liste
                nombre1 = resultat
                print("historique :", historique)
                print("total :",resultat)
                opérateur = input("entrez l'opérateur : ").lower()
                if opérateur.isalpha():

                    if opérateur != "q" and opérateur !="c":

                        print("Veuillez entrez des chiffres valides")
                        run = False
                    else:

                        clear_variables(opérateur)
                        quitter(opérateur)
                        run = False
                elif est_operateur(opérateur):

                    nombre2 = input("Entrez un chiffre : ").lower()
                    if nombre2.isalpha() or est_operateur(nombre2):

                        if nombre2 != "q" and nombre2 !="c":

                            print("Veuillez entrez des chiffres valides")
                            run = False
                        else:

                            clear_variables(nombre2)
                            quitter(nombre2)
                            run = False
                    else:

                        liste +=str(opérateur) + str(nombre2) 

                        resultat=calcul(opérateur,nombre1,nombre2)
                else:
                    print(f"{opérateur} n'est pas un opérateur valide.")
                    run = False
            continue
        continue




calculatrice()