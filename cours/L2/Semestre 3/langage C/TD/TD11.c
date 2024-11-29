# include <stdio.h>

// exercice 1

/*

Tableau : quand on connait la taille du tableau
allocation dynamique : quand on ne connait pas la taille du tableau
liste chaine : quand on ne connait pas la taille du tableau et qu'on veut ajouter ou supprimer des elements

*/

struct _noeud
{
    int element;
    struct _noeud *suivant;
    
};

typedef struct _noeud noeud;

// exercice 2

int occurence(noeud *tete, int n)
{
    int occurence = 0;
    noeud *courant = tete;
    while (courant != NULL)
    {
        if (courant->element == n)
        {
            occurence++;
        }
        courant = courant->suivant;
    }
    return occurence;
}

int occurence_rec(noeud *tete, int nb){
    if (tete == NULL) {
        return 0;
    }
    return (tete->element == nb) + occurence_v2(tete->suivant, nb);

}