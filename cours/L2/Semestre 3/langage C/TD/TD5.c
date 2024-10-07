# include <stdio.h>

int nb_bit(int nb) {
    if (nb == 0) {
        return 0;
    }
    else {
        if (nb & 1 ){
            return nb_bit_a_1(nb >> 1);
        }
        else{
            return nb_bit_a_1(nb >> 1) + 1;
        }
    }
}


int nb_bit2(int nb){
    if (nb == 0){
        return 0;
    }
    return (nb % 2) + nb_2(nb/2);
}



int main(void){
    nb_bit(14);
}

