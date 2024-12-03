# include <stdio.h>
# include <stdlib.h>


struct noeud
{
    int valeur;
    struct noeud *suivant;
};
typedef struct _noeud noeud;


// exerice 1


int insere_element_debut(struct noeud **tete, int valeur){
    struct noeud *nouveau = malloc(sizeof(struct noeud));
    if (nouveau == NULL){
        return 0;
    }
    nouveau->valeur = valeur;
    nouveau->suivant = *tete;
    *tete = nouveau;
    return 1;
}

// exerice 2

int imprime_liste(struct noeud *tete){
    struct noeud *courant = tete;
    while (courant != NULL){
        printf("%d ", courant->valeur);
        courant = courant->suivant;
    }
    printf("\n");
    return 1;
}

// exerice 3

int imprime_liste_rec(struct noeud *tete){
    if (tete == NULL){
        printf("\n");
        return 0;
    }
    printf("%d ", tete->valeur);
    imprime_liste_rec(tete->suivant);
    return 1;
}   

// exerice 5
int imprime_liste_inverse_rec(struct noeud *tete) {
    if (tete == NULL) {
        return 0;
    }
    imprime_liste_inverse_rec(tete->suivant);
    printf("%d ", tete->valeur);
    return 1;
}

// exerice 6

int supprime_element_debut(struct noeud **tete){
    if (*tete == NULL){
        return 0;
    }
    struct noeud *temp = *tete;
    *tete = (*tete)->suivant;
    free(temp);
    return 1;
}

// exerice 7

int supprime_element(struct noeud **tete, int valeur){
    struct noeud *courant = *tete;
    struct noeud *precedent = NULL;
    while (courant != NULL && courant->valeur != valeur){
        precedent = courant;
        courant = courant->suivant; 
    }
    if (courant == NULL){
        return 0;
    }
    if (precedent == NULL){
        *tete = courant->suivant;
    }else{
        precedent->suivant = courant->suivant;
    }
    free(courant);
    return 1;
}       







/*              TEST              */
int main(void){
    struct noeud *tete = NULL;
    insere_element_debut(&tete, 1);
    insere_element_debut(&tete, 2);
    insere_element_debut(&tete, 3);
    insere_element_debut(&tete, 4);
    printf("Exercice 2\n");
    imprime_liste(tete);
    printf("Exercice 3\n");
    imprime_liste_rec(tete);
    printf("Exercice 5\n");
    imprime_liste_inverse_rec(tete);
    supprime_element_debut(&tete);
    printf("\nSuppression du premier element\n");
    printf("liste apres suppression : ");
    imprime_liste(tete);

    return 0;

}