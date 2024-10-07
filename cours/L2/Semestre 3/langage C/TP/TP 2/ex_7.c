#include <stdio.h>


int main (void)
{
    int i = 5, j = 2;
    float f, f2, f3;
    f = 4*(i/j);
    f2 = 4*(float)(i/j);
    f3 = 4* ((float )i /(float)j);
    printf("la valeur de f est: %f \n", f);
    printf("la valeur de f, apres une application globale de l'operateur cast, est: %f \n", f2);
    printf("la valeur de f, apresdes applications locaux de l'operateur cast,  est: %f \n", f3);
}
