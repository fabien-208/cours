# include <stdio.h>   

// exercice 1

int entier_palindrome(int n) {
   int original = n;
   int reverse = 0;
   int truc;

   while (n != 0) {
      truc = n % 10;
      reverse = reverse * 10 + truc;
      n /= 10;
   }

   return original == reverse;
}

// exercice 2

int puissance_de_deux(int n){
   if (n == 0){
      return 0;
   }
   else {
      if (n == 1){
         return 1;
      }
      if (n & (n - 1)) {
         return 0;
      } else{
         puissance_de_deux(n>>1);
      }
   }

}


// exercice 3


int puissance_de_deux_2(int n){
   while (n >= 1){
      if (n == 1){
         return 1;
      }
      if (n == 0){
         return 0;
      }
      if (n & (n - 1)) {
         return 0;
      }
      n = n >> 1;
   }
}



// exercice 4

int truc (void){
   unsigned char i;
   unsigned short int j=256;
   for (i=0; i!=j; i++){
      printf ("Le caractère numéro %d est : %c \n", i, i);
   }
   return (0);
}



// exercice 5

int compter_chiffre(int c, int n) {
    int nb = 0;

   for (int i = 0; i <= n; i++) {
      int num = i;
      while (num != 0) {
         if (num % 10 == c) {
            nb++;
         }
         num /= 10;
      }
   }
   return nb;
}


// exercice 6

int chiffrement_subtitusion(int k, char m){
   
   m += k;
   if (m >= 'Z' ){
      m-= 26;
   }
   return m;
}

int dechiffrement_subtitusion(int k, char m){
   m -=k;
   if (m < 'A'){
      m+= 26;
   }
   return m;

}


// exerice 7

int ex_7(void){
   int i=-20;
   int *p1;
   int **p2;
   int ***p3;
   int ****p4;
   p1=&i;
   p2=&p1;
   p3=&p2;
   p4=&p3;
   printf ("La valeur de i est : %d.\n ", ****p4);
   return (0);
}


// exercice 8




int main(void){
   printf("%d\n", entier_palindrome(45652));
   printf("%d\n", entier_palindrome(35453));
   printf("%d\n", puissance_de_deux(134));
   printf("%d\n", puissance_de_deux_2(128));
   //truc();
   printf("%d\n", compter_chiffre(7, 100));
   printf("%c\n", chiffrement_subtitusion(2,'A'));
   printf("%c\n", chiffrement_subtitusion(4,'W'));
   printf("%c\n", dechiffrement_subtitusion(2,'D'));
   printf("%c\n", dechiffrement_subtitusion(2,'A'));
   ex_7();
   

}