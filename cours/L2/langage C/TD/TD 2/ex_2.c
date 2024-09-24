# include <stdio.h>

/*
int main(void){
    char n;
    int i= 0;
    printf("entrer un texte: ");
    scanf("%c", &n);
    while (n != '\n'){
        scanf("%c", &n);
        i++;
    }
    printf("%c", i);
    return(0);
       
}
*/

int main (void){
    int i = 0;
    while (getchar() != '\n'){
        i++;
    }
    printf("%c", i);
    return(0);
}