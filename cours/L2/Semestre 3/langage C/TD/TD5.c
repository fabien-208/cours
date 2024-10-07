# include <stdio.h>

// exercice 1

int nb_bit(int nb) {
    if (nb == 0) {
        return 0;
    }
    else {
        if (nb & 1 ){
            return nb_bit(nb >> 1);
        }
        else{
            return nb_bit(nb >> 1) + 1;
        }
    }
}

// exercice 2


int nb_bit2(int nb){
    if (nb == 0){
        return 0;
    }
    return (nb % 2) + nb_bit2(nb/2);
}


// exercice 3

int div_de_n(int n) {
    int i = 1;
    int div = 0;
    while (i < n) {
        if(n/i == 0){
            div++;
        }
        i++;
    }
    return div;
}

// exercice 6


int puissance(int a , int b){
    unsigned int som = 0;
    for(int i = 1;i <= b;i++){
        som += a*a;
    }
    return som;
}
