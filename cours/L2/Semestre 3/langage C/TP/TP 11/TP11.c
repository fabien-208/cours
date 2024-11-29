# include <stdio.h>
# include <string.h>
# include <stdlib.h>

// exercice 1

float copier_un_real_v1(float b){
    float a;
    a= b;
    return a;
}
void copier_un_real_v2(float *a, float b){
    *a = b;
}
void copier_un_real_v3(float *a, float *b){
    *a =*b;
}
void copier_un_tableau(int a[], int b[], int n){
    int i;
    for (i=0;i<n;i++) a[i] = b[i];
}

float copier_un_real_v1_sans_egal(float b){
    float a;
    memcpy(&a, &b, sizeof(float));
    return a;
}

void copier_un_real_v2_sans_egal(float *a, float b){
    memcpy(a, &b, sizeof(float));
}

void copier_un_real_v3_sans_egal(float *a, float *b){
    memcpy(a, b, sizeof(float));
}

void copier_un_tableau_sans_egal(int a[], int b[], int n){
    memcpy(a, b, n * sizeof(int));
}



// exercice 2


int majuscule(const char c){
    return (c >= 'A' && c <= 'Z') ? 1 : 0;
}

int compte_majuscule(const char *s){
    int count = 0;
    while (*s) {
        if (majuscule(*s)) {
            count++;
        }
        s++;
    }
    return count;
}


// exercice 3
int comparer_chaines(const char *s1, const char *s2) {
    while (*s1 && *s2) {
        if (*s1 < *s2) {
            return -1;
        } else if (*s1 > *s2) {
            return 1;
        }
        s1++;
        s2++;
    }
    if (*s1 < *s2) {
        return -1;
    } else if (*s1 > *s2) {
        return 1;
    }
    return 0;
}


// exercice 4

struct _noeud{
    int element;
    struct _noeud *suivant;
};

typedef struct _noeud noeud;

void imprimer_liste(noeud *tete){
    while (tete) {
        printf("%d ", tete->element);
        tete = tete->suivant;
    }
    printf("\n");
}


// exercice 5

noeud *creation_de_liste(void){
    noeud *tete = NULL;
    noeud *nouveau;
    int valeur;

    printf("Entrez des entiers (nombre négatif pour arrêter) :\n");
    while (1) {
        scanf("%d", &valeur);
        if ((valeur < 0 || valeur > 9)) {
            break;
        }  
        nouveau = (noeud *)malloc(sizeof(noeud));
        nouveau->element = valeur;
        nouveau->suivant = tete;
        tete = nouveau;
    }
    return tete;
};


void creation_de_liste_v2(noeud **tete){
    noeud *nouveau;
    int valeur;

    printf("Entrez des entiers (nombre negatif pour arreter) :\n");
    while (1) {
        scanf("%d", &valeur);
        if ((valeur < 0 || valeur > 9)) {
            break;
        }   
        nouveau = (noeud *)malloc(sizeof(noeud));
        nouveau->element = valeur;
        nouveau->suivant = *tete;
        *tete = nouveau;
    }
};

// exercice 7

int existe(noeud *tete, int nb){
    while (tete) {
        if (tete->element == nb) {
            return 1;
        }
        tete = tete->suivant;
    }
    return 0;
}


int existe_v2(noeud *tete, int nb){
    int n = 0;
    while (tete) {
        if (tete->element == nb) {
            return n;
        }
        tete = tete->suivant;
        n++;
    }
    return NULL;
}


/*          TEST            */

int main(){
    char c = 'A';
    char d = 'b';
    char s[] = "Hello World";
    char s2[] = "Hello World!";
    noeud n1 = {1, NULL};
    noeud n2 = {2, &n1};
    noeud n3 = {3, &n2};
    
    if (majuscule(c)) {
        printf("'%c' est une majuscule\n", c);
    } else {
        printf("'%c' n'est pas une majuscule\n", c);
    }
    if (majuscule(d)) {
        printf("'%c' est une majuscule\n", d);
    } else {
        printf("'%c' n'est pas une majuscule\n", d);
    }
    printf("Il y a %d majuscules dans '%s'\n", compte_majuscule(s), s); 
    printf("la comparaison de '%s' et '%s' donne %d\n", s, s2, comparer_chaines(s, s2));
    imprimer_liste(&n3);
    noeud *tete = creation_de_liste();
    imprimer_liste(tete);
    return 0;
}

