#include <stdio.h>

// exercice 1

#define k 5

int tous_differents(unsigned int *t){
    for (int i = 0; i < k; i++){
        for (int j = i + 1; j < k; j++){
            if (t[i] == t[j]){
                return 0;
            }
        }
    }
    return 1;
}


// exercice 2
int somme_positifs_rec(unsigned int *t) {
    if (*t == -1) {
        return 0;
    }
    return *t + somme_positifs_rec(t + 1);
}


// exercice 3

// question 1

int est_egaux(int a , int b) {
    if (a == b) {
        return 0;
    }else if(a < b) {
        return -1;
    }
    return 1;
}

// question 2

int est_egaux_2(unsigned int a,unsigned int b){
    unsigned int sa, sb;
    while(a || b){
        sa  = a, sb = b;
        while(sa && sb){
            sa = sa >> 1;
            sb = sb >> 1;
        }
        if (sa)return 1;
        else if (sb) return -1;
    }
    a = a << 1;
    b = b << 1;
    return 0;
}

int compare(unsigned int a, unsigned int b) {
    unsigned int mask = 1 << (sizeof(unsigned int) * 8 - 1);
    while (mask) {
        if ((a & mask) && !(b & mask)) {
            return 1;
        } else if (!(a & mask) && (b & mask)) {
            return -1;
        }
        mask >>= 1;
    }
    return 0;
}


// exercice 4

# define N 3


int tictactoe_gagnant(int t[N][N]){
    int i, j;
    for (i = 0; i < N; i++){
        if (t[i][0] == t[i][1] && t[i][1] == t[i][2]){
            return t[i][0];
        }
    }
    for (j = 0; j < N; j++){
        if (t[0][j] == t[1][j] && t[1][j] == t[2][j]){
            return t[0][j];
        }
    }
    if (t[0][0] == t[1][1] && t[1][1] == t[2][2]){
        return t[0][0];
    }
    if (t[0][2] == t[1][1] && t[1][1] == t[2][0]){
        return t[0][2];
    }
    return 0;
}














int main(void){
    unsigned int t[k] = {1, 2, 3, 4, 5};
    unsigned int t2[k] = {1, 2, 3, 4, 4};
    unsigned int t3[k] = {1, 2, 3, 4, -1};
    printf("exercice 1\n");
    printf("%d\n", tous_differents(t));
    printf("%d\n", tous_differents(t2));
    printf("\nexercice 2\n");
    printf("%d\n", somme_positifs_rec(t3));
    printf("\nExercice 3\n");
    int a = 16, b = 15;
    printf("a = %d, b = %d\n", a, b);
    printf("%d\n", compare(a, b));
    a = 20, b = 30;
    printf("a = %d, b = %d\n", a, b);
    printf("%d\n", compare(a, b));
    a = 18, b = 18;
    printf("a = %d, b = %d\n", a, b);
    printf("%d\n", compare(a, b));
    return 0;
}

