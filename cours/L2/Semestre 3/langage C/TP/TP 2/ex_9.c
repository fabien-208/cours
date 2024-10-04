/****
Les huitserreurs de compilaion
****/

# include <stdio.h>

int main (void)
{
    int b =1, c, a;
    int f = 0;
    printf("Merci de saisir un premier nombre. \n");
    scanf("%d", &b);
    printf("Merci de saisir un deuxieme nombre. \n");
    scanf("%d", &c);
    a = (b + c);
    f = (a > 1); 
    if (f){
        printf("la somme des deux nombres lus est strictement positive. \n");
    }else{
        printf("la somme des deux nombrees lus est nègatifs\n");
    }
    return(0);
}