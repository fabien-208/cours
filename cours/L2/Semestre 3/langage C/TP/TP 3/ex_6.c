# include <stdio.h>


#include <stdio.h>
int main (void) {
    char h;
    printf("Merci d’introduire la lettre en hexadécimal : ");
    scanf("%c", &h);
    switch (h) {
        case 0:
        printf("Le nombre décimal associé est : %d\n", 0);
        break;
        case 1:
        printf("Le nombre décimal associé est : %d\n", 1);
        break;
        case 2:
        printf("Le nombre décimal associé est : %d\n", 2);
        break;
        case 3:
        printf("Le nombre décimal associé est : %d\n", 3);
        break;
        case 4:
        printf("Le nombre décimal associé est : %d\n", 4);
        break;
        case 5:
        printf("Le nombre décimal associé est : %d\n", 5);
        break;
        case 6:
        printf("Le nombre décimal associé est : %d\n", 6);
        break;
        case 7:
        printf("Le nombre décimal associé est : %d\n", 7);
        break;
        case 8:
        printf("Le nombre décimal associé est : %d\n", 8);
        break;
        case 9:
        printf("Le nombre décimal associé est : %d\n", 9);
        break;
        case 'A':
        printf("Le nombre décimal associé est : %d\n", 10);
        break;
        case 'B':
        printf("Le nombre décimal associé est : %d\n", 11);
        break;
        case 'C':
        printf("Le nombre décimal associé est : %d\n", 12);
        break;
        case 'D':
        printf("Le nombre décimal associé est : %d\n", 13);
        break;
        case 'E':
        printf("Le nombre décimal associé est : %d\n", 14);
        break;
        case 'F':
        printf("Le nombre décimal associé est : %d\n", 15);
        break;
        default :
        printf("Le nombre décimal associé est : %d\n", -1);
        break;
    }
    return (0);
}