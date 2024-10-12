# include <stdio.h>

int main (void){
    int n, all = 0;
    printf("nombre d' alumettes: ");
    scanf("%d", &n);
    while( n > 0){
        while (all > 3 && all <=0){
            printf("\ntour du joueur 1 nombre d'allumettes a retirer (1, 2 ou 3): ");
            scanf("%d", &all);
        }
        n -= all;
        all = 0;
        if (n <= 0){
            printf("\nle joueur 1 a perdu");
        }
        while (all > 3 && all <=0){
            printf("\ntour du joueur 2 nombre d'allumettes a retirer (1, 2 ou 3): ");
            scanf("%d", &all);
        }
        n -= all;
        all = 0;
        if (n <= 0){
            printf("\nle joueur 2 a perdu");
        }
    }
    return(0);
}w