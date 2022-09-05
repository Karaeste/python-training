import random

reponse = random.randint(0, 101)
essais = 5
choice = 103
print("*** Le jeu du nombre mystère ***")
while essais > 0:
    choice = 103
    while True: 
        if essais == 1:
            print(f"Il te reste {essais} essai")
        else:
            print(f"Il te reste {essais} essais")
        choice = input("Devine le nombre : ")
        if not choice.isnumeric():
            print("Veuillez entrez un nombre valide.")
        else:
            break
    if int(reponse) < int(choice):
        print(f"Le nombre mystère est plus petit que {choice}")
    elif int(reponse) > int(choice):
        print(f"Le nombre mystère est plus grand que {choice}")
    else:
        print(f"Bravo ! Le nombre mystère était bien {reponse} !")
        if essais == 1:
            print(f"Tu as trouvé le nombre en {essais} essai")
            break
        else:
            print(f"Tu as trouvé le nombre en {essais} essais")
            break
    essais -= 1
if essais == 0:
    print(f"Dommage ! Le nombre mystère était {reponse}")
print("Fin du jeu !")
