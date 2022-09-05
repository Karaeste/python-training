from random import randint
hp_player = hp_enemy = 50
player_potions = 3
choice = ''
while hp_player > 0 and hp_enemy > 0:
    if choice != '2':
        choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        if choice == '1':
            damage = randint(5, 11)
            hp_enemy -= damage
            print(f"Vous avez infligé {damage} points de dégats")
        elif choice == '2':
            if player_potions > 0:
                heal = randint(15, 51)
                hp_player += heal
                player_potions -= 1
                print(f"Vous récupérez {heal} points de vie ({player_potions} potion{'s' if player_potions > 1 else ''} restante{'s' if player_potions > 1 else ''})")
            else:
                print("Vous n'avez plus de potions ...")
                choice = ''
                continue
        else:
            continue
    else:
        choice = ''
        print("Vous passez votre tour ...")
    if hp_enemy < 1:
        print("Tu as gagné !")
        break
    damage = randint(5, 16)
    hp_player -= damage
    print(f"L'ennemi vous a infligé {damage} points de dégats.")
    if hp_player < 1:
        print("Tu as perdu !")
        break
    print(f"Il vous reste {hp_player} point{'s' if hp_player > 1 else ''} de vie.")
    print(f"Il reste {hp_enemy} point{'s' if hp_enemy > 1 else ''} de vie à l'ennemi.")
    print("____________________________________________________________________________________________")
print("Fin du jeu.")