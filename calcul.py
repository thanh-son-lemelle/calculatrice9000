import ast
import operator

historique = []
liste = ""
resultat = ""
nombre1 = ""
nombre2 = ""
opérateur = ""

# Dictionnaire des opérateurs
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.FloorDiv: operator.floordiv,
}
# Fonction pour évaluer une expression mathématique représentée par un AST (Abstract Syntax Tree)
def evaluate_expression(node):
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = evaluate_expression(node.left)
        right = evaluate_expression(node.right)
        return OPERATORS[type(node.op)](left, right)
    else:
        raise ValueError("Expression invalide")
# Fonction pour analyser et évaluer une expression mathématique sous forme de chaîne de caractères
def parse_and_evaluate(expression):
    global test_parse_and_evaluate
    try:
        tree = ast.parse(expression, mode='eval')
        result = evaluate_expression(tree.body)
        return result
    except (SyntaxError, ValueError) as e:
        print(f"Erreur lors de l'évaluation de l'expression : {str(e)}")
        return None
# Fonctions pour les opérations mathématiques de base
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
    
def modulo (x , y):
    if y != 0:
        return float(x) % float(y)
    else:
        return "Erreur: Division par zéro"
    
def floordivision (x , y):
    if y != 0:
        return float(x) // float(y)
    else:
        return "Erreur: Division par zéro"

def puissance(x, y):
    return float(x)**float(y)
# Fonction pour reset les variables et recommencer un calcul
def clear_variables(x):
        global historique, liste, resultat, nombre1, nombre2, opérateur
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

# Fonctions pour les calculs de base
def calcul(opérateur,nombre1,nombre2):
    global historique, liste, resultat


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
    elif opérateur == "%":
        resultat = modulo(nombre1,nombre2)
    elif opérateur == "//":
        resultat = floordivision(nombre1,nombre2)

    return resultat

# Fonction qui vérifie si l'opérateur et un  opérateur valide
def est_operateur(val):
    operateurs_valides = ['+', '-', '*', '/', '**']

    return val in operateurs_valides

# Fonction pour sauvegarder l'historique dans un fichier txt lorsque l'utilisateur quitte
def sauvegarder_historique():
    global historique
    if historique == []:
        print("L'historique est vide.")
        return
    try:
        with open("historique.txt", "w") as file:
            for calcul in historique:
                file.write(calcul + f" = {resultat}" "\n")
        print("L'historique a été enregistré dans le fichier historique.txt.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de l'historique : {str(e)}")
    pass

# Fonction pour quitter le programme
def quitter(x):
    if x == "q":
        while True:
            reponse = input("Voulez-vous quitter ? (y/n): ").lower()
            if reponse == 'y':
                sauvegarder = input("Voulez-vous enregistrer l'historique dans un fichier ? (y/n): ").lower()
                if sauvegarder == 'y':
                    sauvegarder_historique()
                print("Au revoir!")
                exit()
            elif reponse == 'n':
                print("Continuons...")
                calculatrice()
            else:
                print("Réponse non valide. Veuillez entrer 'y' pour oui ou 'n' pour non.")
    else:
        return

# Fonction principal
def calculatrice():
    global resultat, test_parse_and_evaluate
    print("Bienvenue dans la calculatrice ! Entrez 'q' pour quitter ou 'c' pour effacer.")

    while True: # Boucle principal

        run = True
        while run: # Boucle qui s'arrête si un input n'est pas valide
            test_parse_and_evaluate = False
            # Demande à l'utilisateur de rentrer deux nombres
            if resultat == "": # Vérifie si on à pas fait de calcule pour demander deux 'nombres' à calculer

                nombre1 = input("Entrez un chiffre : ").lower()  
                if nombre1.isalpha() or est_operateur(nombre1): # Vérifie si nombre1 est un caractère alphabétique ou un opérateur

                    if nombre1 != "q" and nombre1 !="c": # Si ce n'est pas un caractère (alphabétique) valide

                        print("Veuillez entrez des chiffres valides")
                        run = False
                    else:                               # Sinon ....

                        clear_variables(nombre1) # On vérifie la fonction clear puis quitter
                        quitter(nombre1)
                        run = False
                else:

                    opérateur = input("entrez l'opérateur : ").lower() # on entre l'opérateur
                    if opérateur.isalpha(): # Si caractère alphabétique on ...

                        if opérateur != "q" and opérateur !="c": # Si ce n'est pas un caractère (alphabétique) valide

                            print("Veuillez entrez des chiffres valides")
                            run = False
                        else:                               # Sinon ....


                            clear_variables(opérateur) # On vérifie la fonction clear puis quitter
                            quitter(opérateur)
                            run = False
                    elif est_operateur(opérateur): # Sinon on vérifie la condition opérateur avec la fonction est opérateur et on ....
                        print(f"{opérateur} est un opérateur valide.")

                        nombre2 = input("Entrez un chiffre : ").lower()  # on entre le deuxième nombre
                        if nombre2.isalpha() or est_operateur(nombre2): # Vérifie si nombre1 est un caractère alphabétique ou un opérateur

                            if nombre2 != "q" and nombre2 !="c": # Si ce n'est pas un caractère (alphabétique) valide


                                print("Veuillez entrez des chiffres valides")
                                run = False
                            else:                           # Sinon ....

                                clear_variables(nombre2) # On vérifie la fonction clear puis quitter
                                quitter(nombre2)
                                run = False
                        else:                               # Sinon ....

                            liste = str(nombre1) + str(opérateur) + str(nombre2) # On enregistre dans une variable en tant que chaine de caractère
                            historique.append(liste) # On ajoute la liste dans historique liste
                            nombre1 = parse_and_evaluate (nombre1) # On traite nombre1 en tant que chaine de caractère pour voir si il ya une opération mathématique et on fait le calcule si il y'en a un
                            nombre2 = parse_and_evaluate (nombre2) # On traite nombre2 en tant que chaine de caractère pour voir si il ya une opération mathématique et on fait le calcule si il y'en a un
                            resultat = calcul(opérateur,nombre1,nombre2) # on fait le calcul de base entre nombre1 et nombre2
                    else:                                   # Si ce n'était pas un opérateur saisie en tant qu'opérateur ...
                        print(f"{opérateur} n'est pas un opérateur valide.")
                        run = False

            elif resultat != "": # Si un calcul a déja été effectuer 
                
                historique [0]= liste # On enregistre la liste dans l'historique index 0
                nombre1 = resultat  # nombre1 prend la valeur du résultat
                print("historique :", historique) # On affiche le calcul précédent
                print("total :",resultat)   # On affiche le résultat 
                opérateur = input("entrez l'opérateur : ").lower() # On rentre un nouvel opérateur
                if opérateur.isalpha(): # Si caractère alphabétique on ...

                    if opérateur != "q" and opérateur != "c": # Si ce n'est pas un caractère (alphabétique) valide

                        print("Veuillez entrez des chiffres valides")
                        run = False
                    else:                               # Sinon ....

                        clear_variables(opérateur)  # On vérifie la fonction clear puis quitter
                        quitter(opérateur)
                        run = False
                elif est_operateur(opérateur): # Sinon on vérifie la condition opérateur avec la fonction est opérateur et on ....

                    nombre2 = input("Entrez un chiffre : ").lower()
                    if nombre2.isalpha() or est_operateur(nombre2): # Vérifie si nombre1 est un caractère alphabétique ou un opérateur

                        if nombre2 != "q" and nombre2 !="c": # Si ce n'est pas un caractère (alphabétique) valide

                            print("Veuillez entrez des chiffres valides")
                            run = False
                        else:                           # Sinon ....

                            clear_variables(nombre2)    # On vérifie la fonction clear puis quitter
                            quitter(nombre2)
                            run = False
                    else:

                        liste += str(opérateur) + str(nombre2) # On ajoute à la liste l'opérateur et le nombre2 nouvellements entrés
                        nombre2 = parse_and_evaluate(nombre2) # On traite nombre2 en tant que chaine de caractère pour voir si il ya une opération mathématique et on fait le calcule si il y'en a un

                        resultat=calcul(opérateur,nombre1,nombre2) # on fait le calcul de base entre nombre1 et nombre2
                else:
                    print(f"{opérateur} n'est pas un opérateur valide.")
                    run = False
            continue
        continue




calculatrice()