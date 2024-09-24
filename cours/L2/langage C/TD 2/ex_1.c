#include <stdio.h>

int main (void)
{
    unsigned short entier;
    unsigned char c;
    printf("\n Merci de rentrer un entier et ensuite de renter un caractere : ");
    scanf("%hu", &entier);
    c = getchar();
    printf("l'entier rentré est : %d\n", entier);
    printf("le caractère est : %d\n", c);
    return(0);
}