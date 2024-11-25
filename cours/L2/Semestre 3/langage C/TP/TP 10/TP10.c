# include <stdio.h>
# include <string.h>


// exercice 1


int exercice_1(void) {
    int t[3]={10, -20 ,320};
    printf ("les adresses de t et de t+1 sont : %p et %p \n", &t, &t+1);
    printf ("les adresses de t[0] et t[0]+1 sont : %p et %p\n", &t[0], &t[0]+1);
    printf ("les valeurs de t et t+1 sont : %p et %p \n", t, t+1);
    return 0;
}


// exercice 2


int nbre_mot_de_taille_n(char *ch, int n ){
    int re = 0;
    int len = strlen(ch);
    int count = 0;
    for (int i = 0; i < len; i++) {
        if (ch[i] != ' ') {
            count++;
        } else {
            if (count == n) {
                re++;
            }
            count = 0;
        }
    }
    if (count == n) {
        re++;
    }
    return re;
}

// exercice 3

const char * strstr_fin(const char * grande, const char * petite) {
    const char *result = NULL;
    const char *temp = grande;
    size_t petite_len = strlen(petite);

    if (petite_len == 0) {
        return grande;
    }

    while ((temp = strstr(temp, petite)) != NULL) {
        result = temp;
        temp++;
    }

    return result;
}


// exercice 4
#define N 8

char echiquier[N][N];

void initialiser_echiquer(void) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            echiquier[i][j] = ' ';
        }
    }
}


void imprimer_echiquier(void) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("|%c", echiquier[i][j]);
        }
        printf("|\n");
    }
}



/*                        TEST                         */

int main(void){
    const char *grande = "Ceci est un exemple de texte avec exemple a la fin exemple";
    const char *petite = "avec";
    const char *result = strstr_fin(grande, petite);
    
    int n = 4;
    char ch[] = "bonjour vous avez pris place dans le train le plus rapide au monde";
    printf("Exercice 2\n");
    printf("Dans cette chaine de caractere il y a %d mots de taille %d\n", n, nbre_mot_de_taille_n(ch, n));
    n = 7;
    printf("Dans cette chaine de caractere il y a %d mots de taille %d\n", n, nbre_mot_de_taille_n(ch, n));
    printf("Exercice 3\n");
    if (result) {
        printf("La derniere occurrence de '%s' se trouve a l'adresse : %p\n", petite, result);
        printf("La sous-chaine trouvee est : %s\n", result);
    } else {
        printf("La sous-chaine '%s' n'a pas été trouvée.\n", petite);
    }
    printf("Exercice 4\n");
    initialiser_echiquer();
    imprimer_echiquier();

}