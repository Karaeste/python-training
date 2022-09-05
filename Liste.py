array = []
leave = 0
while leave == 0:
    print("Choisissez parmi les 5 options suivantes :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément à la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")
    choice = input("-> Votre choix : ")
    if choice == "1":
        new_element = input("Entrez le nom d'un élément à ajouter à la liste de couses : ")
        array.append(new_element)
        print(f"L'élément {new_element} a bien été ajouter à la liste.")
    elif choice == "2":
        remove_element = input("Entrez le nom de l'élément à retirer à la liste de courses : ")
        if array.count(remove_element) == 0:
            print(f"L'élément {remove_element} n'est pas dans la liste.")
        else:    
            array.remove(remove_element)
            print(f"L'élément {remove_element} a bien été retirer à la liste.")
    elif choice == "3":
        if array:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(array, 1):
                print(f"{i}. {item}")
        else:
            print("Votre lise ne contient aucun élément.")
    elif choice == "4":
        array.clear()
        print("La liste a été vidée de son contenu.")
    elif choice == "5":
        print("A bientôt !")
        break
    else:
        print("Veuillez choisir une option valide.")
    print("________________________________________________________________________________________________\n")