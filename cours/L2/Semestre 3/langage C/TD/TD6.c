#include <stdio.h>

// exercice 1

int puissance(int a, int b) {
    int result = 1;
    for (int i = 0; i < b; i++) {
        result *= a;
    }
    return result;
}

int puissance_rec(int a, int b){
    if (b == 0) {
        return 1;
    }
    if (b %2 == 1){
        return a * puissance_rec(a, b-1);
    } else {
        return puissance_rec(a, b/2) * puissance_rec(a, b/2);
    }
    
}


// exercice 2


int mystere(int n){
    int i;
    double s = 0;
    for (i = 1; i <= n; i++){
        s += i/n;
    }
    return s;    
}

// exercice 3


int f(int *a, int n){
    if (n==1){
        return 1;
    }
    if (a[0] > a[1]){
        return 0;
    }
    else{
        return f(a+1, n-1);
    }
}








int main() {
    printf("%d\n", puissance(2, 3));
    printf("%d\n", puissance_rec(2, 3));
    printf("%d\n", mystere(2345));
}