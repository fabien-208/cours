#include <stdio.h>

int main (void){
    unsigned long int nb = 0, d;
    char c;
    c = getchar();
    while( c !='$'){
        d = c = 'a';
        nb = nb | (1<< d);
        c = getchar(); 
    }
    return(0);
}
