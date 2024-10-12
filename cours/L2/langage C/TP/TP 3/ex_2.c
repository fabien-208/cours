# include <stdio.h>


// partie 1
/*

int main (void){
    int nb = 0;
    char c;
    printf("veuillez entrer un texte : ");
    while ( c= getchar() != '\n'){
        nb++;
    }
    printf("il y a %d caractere dans la phrase", nb);
    return(0);
}

*/


//partie 2


int main (void) {
    unsigned char c;
    printf("veuillez entrer un texte : ");
    while ( getchar() != '\n'){
        c++;
    }
    printf("il y a %d caractere dans la phrase", c);
    return(0);
}