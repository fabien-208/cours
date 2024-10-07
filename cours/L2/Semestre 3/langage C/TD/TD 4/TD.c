#include <stdio.h>

int ex_1 (void){
    char car;
    printf ("\nMerci d'introduire une lettre majuscule ou minuscule: ");
    scanf ("%c", &car);
    printf ("\nLa conversion (majuscule vs minuscule) de %c donne %c.\n ",car, car + ((car>='A') && (car<='Z')) ? car -'A' + 'a' : car + 'a'-'A');
    return(0);

}

int ex_2(int n){
    int truc = 0;
    while(n !=0){
        truc = truc + (n % 10);
        n = n / 10;
    }
    // printf("%d", truc);
    return(truc);
}

int ex_2_2(int n){
    int i;
    for(i = 1800; i<=n; i++){
        if (ex_2(i) == n-i){
            printf("%d\n", i);
        }
    }
    return(0);
}

int ex_3(int n){
    return(0);
}


int main(void){
    //ex_1();
    //printf("%d", ex_2(2095));
    ex_2_2(2014);

}
