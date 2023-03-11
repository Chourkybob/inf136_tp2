from constantes import JOUEUR
from constantes import ORDINATEUR
from flotte import flotte_calculer_vie


def jeu_afficher_jouer_courant(identifiant_courant):

    if identifiant_courant == JOUEUR:
        print('C\'est au tour du joueur')

    elif identifiant_courant == ORDINATEUR:
        print('C\'est au tour de l\'ordinateur')

def jeu_joueur_saisir_position_tir():

    while
    i = input(int(''))


    return i,j

def jeu_est_partie_terminee(flotte_1,flotte_2):
    """
    Détermine si une partie est terminée. Si la vie d'une des flottes est égale à zéro, cela indique que la partie est
    complétée.

    Arguments :
        flotte_1 [list] : une flotte de navires du premier joueur.
        flotte_2 [list] : une flotte de navires du deuxième joueur.

    Retourne  :
        [bool] : indicateur de fin de partie.
    """

    # Calculer la vie des flottes 1 et 2 avec la fonction flotte_calculer_vie.
    vie_flotte_1 = {flotte_calculer_vie(flotte_1)}
    vie_flotte_2 = {flotte_calculer_vie(flotte_2)}

    # Comparer la vie des flottes 1 et 2 avec un booléen.
    if  vie_flotte_1 == 0 or vie_flotte_2 == 0:

        # Retoruner Vrai si la partie est terminée, c'est-à-dire lorsque la vie d'une des deux flottes correspond à 0.
        return True

    else:

        # Retourner Faux si la partie continue.
        return False


def jeu_afficher_vainqueur(flotte_joueur):
    """
    Annonce le vainqueur de la partie en affichant le message final.

    Arguments :
        flotte_joueur [list] : correspond à la flotte de navires du joueur

    Retourne  :
        Rien.
    """

    # pas sur de cette etape a voir faut il appeler lautre fonction ou faire une somme
    if flotte_joueur == 0 :

        # Afficher le message vainqueur de l'ordinateur contre le joueur.
        print('C\'est l"ordinateur qui a gagné! Désolé, il faudrait se pratiquer davantage.')

    else:

        # Afficher le message vainqueur du joueur contre l'oridnateur.
        print('C\'est le joueur qui a gagné. Félicitations!')