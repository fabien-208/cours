#include <stdio.h>

// exercice 1

#define k 3

int est_carre_magique(int tableau[k][k]) {
    int somme = 0;
    for (int j = 0; j < 3; j++) {
        somme += tableau[0][j];
    }
    for (int i = 0; i < 3; i++) {
        int somme_ligne = 0, somme_colonne = 0;
        for (int j = 0; j < 3; j++) {
            somme_ligne += tableau[i][j];
            somme_colonne += tableau[j][i];
        }
        if (somme_ligne != somme || somme_colonne != somme) {
            return 0;
        }
    }

    return 1;
}

// exercice 2

// question 1

int est_egaux(int a , int b) {
    if (a == b) {
        return 0;
    }else if(a < b) {
        return -1;
    }
    return 1;
}

// question 2

int est_egaux_2(unsigned int a,unsigned int b){
    unsigned int sa, sb;
    while(a || b){
        sa  = a, sb = b;
        while(sa && sb){
            sa = sa >> 1;
            sb = sb >> 1;
        }
        if (sa)return 1;
        else if (sb) return -1;
    }
    a = a << 1;
    b = b << 1;
    return 0;
}









int main() {
    printf("\nExercice 1\n\n");
    int tableau[3][3] = {{2, 7, 6}, {9, 5, 1}, {4, 3, 8}};
    printf("%d\n", est_carre_magique(tableau));
    printf("\n");
    printf("Exercice 2\n\n");
    int a = 5, b = 5;
    printf("a = %d, b = %d\n", a, b);
    printf("%d\n", est_egaux(a, b));
    a = 7;
    printf("a = %d, b = %d\n", a, b);
    printf("%d\n", est_egaux(a, b));
    a = 3;
    printf("a = %d, b = %d\n", a, b);
    printf("%d\n", est_egaux(a, b));
    printf("\n");
    return 0;
}