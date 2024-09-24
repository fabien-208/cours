#include <stdio.h>
/*
int main (void)

{
    unsigned short i;
    printf(" Entrer un code ASCII : ");
    scanf("%hu", &i);
    printf("la caractère ASCII %hu est: %c \n",i, i);
    return (0);
}



int main (void)
{
    char c;
    printf("Entrer un caractère: ");
    c=getchar();
    printf("le code ASCII du caractère %c est : %d (en décimal), %o (en octal), %x (en héxadécimal)\n", c, c, c, c);
    return(0);
}

*/

int main (void)
{
    unsigned short i;
    char c;
    printf(" Entrer un code ASCII: ");
    scanf("%hu", &i);
    printf("la caractère ASCII %hu est: %c \n", i, i);
    printf("Entrer un caractère: ");
    while (getchar()!='\n');
    c=getchar();
    printf("le code ASCII du caaractère %c est: %d (en décimal), %o (en octal), %x (en héxadécimal minuscule), %X (en héxidémal majuscule)\n", c, c, c, c, c);
    return (0);
}