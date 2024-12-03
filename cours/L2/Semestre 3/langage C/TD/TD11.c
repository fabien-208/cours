# include <stdio.h>
# include <stdlib.h>

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
    return (tete->element == nb) + occurence_rec(tete->suivant, nb);

}


// exercice 3


noeud *creation_de_liste(void){
    noeud *tete = NULL;
    noeud *nouveau;
    int valeur;

    printf("Entrez des entiers (nombre negatif pour arreter) :\n");
    scanf("%d", &valeur);
    while (valeur >= 0) {
        scanf("%d", &valeur);
        if ((valeur < 0)) {
            return tete;
        }  
        nouveau = (noeud *)malloc(sizeof(noeud));
        if (nouveau == NULL) {
            printf("Erreur d'allocation de memoire\n");
            return NULL;
        }
        nouveau->element = valeur;
        nouveau->suivant = tete;
        tete = nouveau;
    }
    return tete;
};




void creation_de_liste_v2(noeud **tete){
    noeud *nouveau;
    int valeur;

    printf("Entrez des entiers (nombre negatif pour arreter) :\n");
    while (1) {
        scanf("%d", &valeur);
        if (valeur < 0) {
            break;
        }   
        nouveau = (noeud *)malloc(sizeof(noeud));
        nouveau->element = valeur;
        nouveau->suivant = *tete;
        *tete = nouveau;
    }
};