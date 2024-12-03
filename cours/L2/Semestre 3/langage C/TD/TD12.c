#include <stdio.h>
#include <stdlib.h>

struct noeud
{
    int valeur;
    struct noeud *suivant, *precedent;
};

typedef struct noeud noeud;

int existe_rec(noeud *tete, int nb)
{
    if (tete == NULL)
        return 0;
    if (tete->valeur == nb)
        return 1;
    return existe_rec(tete->suivant, nb);
}

// exercice 2

void liberer_toute_liste(noeud *tete){
    noeud *temp;
    while (tete != NULL){
        temp = tete;
        tete = tete->suivant;
        free(temp);
    }
}


// exercice 3

void rajouter_element_debut(noeud **tete, int nb){
    noeud *nouveau = malloc(sizeof(noeud));
    if (nouveau == NULL){
        printf("Erreur d'allocation de mémoire\n");
        exit(1);
    }
    nouveau->valeur = nb;
    nouveau->suivant = *tete;
    *tete = nouveau;
}


// exercice 4


void rajouter_element_debut_2(noeud **tete, int nb){
    noeud *nouveau = malloc(sizeof(noeud));
    if (nouveau == NULL){
        printf("Erreur d'allocation de mémoire\n");
        exit(1);
    }
    nouveau->valeur = nb;
    nouveau->suivant = *tete;
    nouveau->precedent =NULL;

    if (*tete != NULL )(*tete)->precedent = nouveau;
    *tete = nouveau;

}

// exercice 5

void rajouter_element_fin_rec(noeud **tete, int nb){
    if (*tete == NULL){
        rajouter_element_debut(tete, nb);
    }else{
        rajouter_element_fin_rec(&((*tete)->suivant), nb);
    }
}




// exercice 6

void rajouter_element_trie_rec(noeud **tete, int nb){
    if (*tete == NULL || (*tete)->valeur > nb){
        rajouter_element_debut(tete, nb);
    }else{
        rajouter_element_trie_rec(&((*tete)->suivant), nb);
    }
}




// test


int main() {
    noeud *tete = NULL;
    rajouter_element_debut(&tete, 3);
    rajouter_element_debut(&tete, 1);
    rajouter_element_debut(&tete, 2);
    printf("Existe 1: %d\n", existe_rec(tete, 1)); //  print 1
    printf("Existe 4: %d\n", existe_rec(tete, 4)); //  print 0

    rajouter_element_fin_rec(&tete, 4);
    rajouter_element_fin_rec(&tete, 5);
    rajouter_element_trie_rec(&tete, 0);
    rajouter_element_trie_rec(&tete, 6);

    noeud *current = tete;
    while (current != NULL) {
        printf("%d ", current->valeur);
        current = current->suivant;
    }
    printf("\n");
    liberer_toute_liste(tete);

    return 0;
}