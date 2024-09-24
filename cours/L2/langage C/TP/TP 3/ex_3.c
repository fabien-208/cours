#include <stdio.h>

// Fonction pour vérifier si un nombre est parfait
int est_parfait(int n) {
    int somme = 0;
    for (int i = 1; i <= n / 2; i++) {
        if (n % i == 0) {
            somme += i;
        }
    }
    return somme == n;
}

int main() {
    int n, nb = 0, i = 1;

    printf("Entrez le nombre de nombres parfaits a afficher : ");
    scanf("%d", &n);

    printf("Les %d premiers nombres parfaits sont :\n", n);
    while (nb < n) {
        if (est_parfait(i)) {
            printf("%d\n", i);
            nb++;
        }
        i++;
    }

    return 0;
}
