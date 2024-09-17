# include <stdio.h>

int main (void)
{
    int i = 14;
    printf("%d  |   %x\n", i, i);
    i = i<<1;
    printf("%d  |   %x\n", i, i);
    i = i<<4;
    printf("%d  |   %x\n", i, i);
    i = i >> 1;
    printf("%d  |   %x\n", i, i);
    i = i >> 4;
    printf("%d  |   %x\n", i, i);
    i = i&1;
    printf("%d  |   %x\n", i, i);
    i = i&4;
    printf("%d  |   %x\n", i, i);
    i = i << 1;
    printf("%d  |   %x\n", i, i);
    i = i<<4;
    printf("%d  |   %x\n", i, i);
    return(0);
}