import random

##pip install colorama (pour avoir les textes en couleurs !)
from colorama import Fore, Back, Style

print("Vous allez jouer au jeu du Plus ou Moins de 1 à 9")

player_name = str(input("Entrez votre pseudo : \n"))
if player_name == "aymeric":
    print(Fore.GREEN +"Quand es-ce que tu reviens ?")
    print(Style.RESET_ALL)

e = True
while e:
    party = int(input("{} en combien de parties voulez vous jouer ? (1 à 5) \n".format(player_name)))
    if party < 6:
        e = False
        print("C'est parti pour jouer {party} parties ! \n".format(party = party))
    else:
        print("Choisissez un nombre entre 1 et 5 ! \n")

nb_party = party
while nb_party > 0:
        rand_number = random.randint(0,9)
        print("J'ai choisi mon nombre, à toi de deviner ! ")
        essais_max = 4
        nb_party -= 1
        print("Il nous reste : {} partie(s) ".format(nb_party))
        
        while essais_max > 0:
            player_choice = int(input("{} essaies de deviner: \n".format(player_name)))
            print("{name}, tu as choisis le nombre : {number}".format(name = player_name, number = player_choice))
            if player_choice > rand_number:
                print(Fore.GREEN +"Votre Nombre est plus grand que celui choisi !")
                print(Style.RESET_ALL)

            if player_choice < rand_number:
                print(Fore.RED +"Votre Nombre est plus petit que celui choisi !")
                print(Style.RESET_ALL)
                
            if player_choice == rand_number:
                print(Fore.GREEN +"Tu as réussi !")
                print(Style.RESET_ALL)
                break
            else:
                essais_max -= 1
                print(Fore.RED +"Essaies encore ! Il te reste {} essais".format(essais_max))
                print(Style.RESET_ALL)
                if essais_max == 0 : 
                    print(Fore.RED +"Tu as gaché tout tes essais !")
                    print(Style.RESET_ALL)
                    break
    