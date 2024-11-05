#include <stdio.h>


int sontDisjoints(int a[], int tailleA, int b[], int tailleB) {
    for (int i = 0; i < tailleA; i++) {
        for (int j = 0; j < tailleB; j++) {
            if (a[i] == b[j]) {
                return 1;
            }
        }
    }
    return 0;
}


int main() {
    int a[] = {1, 2, 3, 4, 5};
    int b[] = {6, 7, 8, 9, 10};
    int c[] = {3, 6, 9};

    int tailleA = sizeof(a) / sizeof(a[0]);
    int tailleB = sizeof(b) / sizeof(b[0]);
    int tailleC = sizeof(c) / sizeof(c[0]);

    if (sontDisjoints(a, tailleA, b, tailleB)) {
        printf("Les tableaux a et b ne sont pas disjoints.\n");
    } else {
        printf("Les tableaux a et b sont disjoints.\n");
    }

    if (sontDisjoints(a, tailleA, c, tailleC)) {
        printf("Les tableaux a et c ne sont pas disjoints.\n");
    } else {
        printf("Les tableaux a et c sont disjoints.\n");
    }

    return 0;
}