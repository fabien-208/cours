#include <stdio.h>

// exercice 1

int estUniforme(int nombre) {
    int dernierChiffre = nombre % 10;
    nombre /= 10;

    while (nombre > 0) {
        if (nombre % 10 != dernierChiffre) {
            return 0;
        }
        nombre /= 10;
    }
    return 1;
}

// exercice 2


int nb_diviseurs(int n){
    int nb_div = 0;
    for (int i = 1; i < n; i++) {
        if (n % i == 0) {
            nb_div++;
        }
    }
    return nb_div;
}


// exercice 3

#define k  5

int fusion(int t1[], int t2[], int t3[]) {
    int i = 0, j = 0, l = 0;
    while (i < k && j < k) {
        if (t1[i] <= t2[j]) {
            t3[l] = t1[i];
            i++;
        } else {
            t3[l] = t2[j];
            j++;
        }
        l++;
    }
    while (i < 5) {
        t3[l] = t1[i];
        i++;
        l++;
    }
    while (j < 5) {
        t3[l] = t2[j];
        j++;
        l++;
    }
    return 0;
}
    

// exercice 4

#include <stdlib.h>

void exercice4() {
    int n;
    printf("Entrez le nombre d'entiers: ");
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Erreur d'allocation de mémoire\n");
        return;
    }

    printf("Entrez %d entiers positifs ou nuls:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int count_zero = 0;
    printf("Nombres nuls: ");
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            count_zero++;
        }
    }
    printf("%d\n", count_zero);

    printf("Nombres pairs: ");
    for (int i = 0; i < n; i++) {
        if (arr[i] != 0 && arr[i] % 2 == 0) {
            printf("%d ", arr[i]);
        }
    }
    printf("\n");

    printf("Nombres impairs: ");
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) {
            printf("%d ", arr[i]);
        }
    }
    printf("\n");

    free(arr);
}

// exercice 5

 int change_bit( int a, int n) {
    if (n < 0 || n >= sizeof(a) * 8) {
        printf("Indice n invalide\n");
        return a;
    }
    return a ^ (1 << n);
}


// test

int main() {
    int nombre = 12;
    printf("\nExercice 1\n");
    printf("%d\n\n", estUniforme(nombre));

    printf("Exercice 2\n");
    printf("%d\n\n", nb_diviseurs(nombre));
    printf("Exercice 3\n");
    int t1[k] = {1, 3, 5, 7, 9};
    int t2[k] = {2, 4, 6, 8, 10};
    int t3[2*k] = {};
    fusion(t1, t2, t3);
    int taille = sizeof(t3) / sizeof(t3[0]);
    printf("Tableau fusionne : { ");
    for (int i = 0; i < taille; i++) {
        printf("%d ", t3[i]);
    }
    printf("}\n");
    printf("\n");
    //printf("Exercice 4\n");   
    //exercice4();
    printf("Exercice 5\n");
    int a = 10;
    int n = 2;
    printf("%d\n", change_bit(a, n));
    printf("\n");

    return 0;
}


