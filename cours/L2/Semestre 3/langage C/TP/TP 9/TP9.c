#include <stdio.h>
#include <stdlib.h>

// Exercice 1

int nb_occ_rec(unsigned int *tab, int nb) {
    if (*tab == -1) {
        return 0;
    }
    return (*tab == nb) + nb_occ_rec(tab+1, nb);
}

// Exercice 2


int mystere2(unsigned int a, unsigned int b){
    unsigned char a_ce_stade=0;
    if (! (a^b)) return 0;
    while (a && b){
        if ((a&1) && (! (b&1))) a_ce_stade=1;
        else if (! (a&1) && (b&1)) a_ce_stade=-1;
        a>>=1;
        b>>=1;
    }
    if (a) return 1;
        else if (b) return -1;
        else return a_ce_stade;
}

// Exercice 3

int exercice3(void){
    int t[3] = {10, -20, 320};
    printf("l'adresse de t est : %p\n", &t);
    printf("l'adresse de t[0] est : %p\n", &t[0]);
    printf("la valeur de t est : %p\n ", t);
    return 0;
}

// Exercice 4


int afficher_tableau(int tableau[], int taille){ 
    printf("Les elements du tableau sont : ["); 
    for (int i = 0; i < taille; i++){ 
        printf("%d, ", tableau[i]); 
    } 
    printf("]\n");
    return 0;
}


int* inverser_tableau(int* tab, int taille) {
    int* tab_inverse = (int*)malloc(taille * sizeof(int));
    if (tab_inverse == NULL) {
        printf("Erreur d'allocation mémoire\n");
        return NULL;
    }
    for (int i = 0; i < taille; i++) {
        tab_inverse[i] = tab[taille - 1 - i];
    }
    afficher_tableau(tab_inverse, taille);
}

// exercice 5

int somme_tab_rec(unsigned int *tab){
    if (*tab == -1){
        return 0;
    }
    else{
        return *tab + somme_tab_rec(tab+1);
    }
}


// exercice 6

int exercice6(void){
    int t[3] = {10, -20, 320};
    printf("la taille de &t est : %lu\n", sizeof(&t));
    printf("la taille de t[0] est : %lu\n", sizeof(t[0]));
    printf("la taille de &t[0] est : %lu\n", sizeof(&t[0]));
    printf("la taille de t est : %lu\n", sizeof(t));
    return 0;
}
// Exercice 7
int est_puissance_de_2(int n) {
    return (n & (n - 1)) == 0;
}



// Main

int main() {
    int tab[] = {1, 2, 3, 4, 2, 2, 5, -1};
    int nb = 2;
    printf("Exercice 1\n");
    printf("nombre d'occurences de %d: %d\n", nb, nb_occ_rec(tab, nb));
    printf("Exercice 2\n");
    int a = 14, b = 14;
    printf(" a = 14, b = 14");
    printf(" mystere2(a, b) = %d\n", mystere2(a, b));
    a = 20;
    b = 55;
    printf(" a = 20, b = 55");
    printf(" mystere2(a, b) = %d\n", mystere2(a, b));
    a = 30;
    b = 12;
    printf(" a = 30, b = 12");
    printf(" mystere2(a, b) = %d\n", mystere2(a, b));
    printf("Exercice 3\n");
    exercice3();
    printf("Exercice 4\n");
    afficher_tableau(tab, 7);
    printf("Tableau inverse\n");
    inverser_tableau(tab, 7);
    printf("Exercice 5\n");
    printf("Somme des elements du tableau t: %d\n", somme_tab_rec(tab));
    printf("Exercice 6\n");
    exercice6();
    printf("Exercice 7\n");
    int n = 16;
    printf("n = 16, est_puissance_de_2(n) = %d\n", est_puissance_de_2(n));
    n = 15;
    printf("n = 15, est_puissance_de_2(n) = %d\n", est_puissance_de_2(n));

    
    return 0;
}