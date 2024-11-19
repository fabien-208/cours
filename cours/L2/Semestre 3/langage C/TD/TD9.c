# include <stdio.h>

// exercice 1

int voyelle (const char c){
    int voyelle[6] = {'a', 'e', 'i', 'o', 'u', 'y'};
    if (c == voyelle[0] || c == voyelle[1] || c == voyelle[2] || c == voyelle[3] || c == voyelle[4] || c == voyelle[5]){
        return 1;
    }
    else{
        return 0;
    }
}

int compte_voyelles (const char *s){
    int i = 0;
    int compteur = 0;
    while (s[i] != '\0'){
        if (voyelle(s[i]) == 1){
            compteur++;
        }
        i++;
    }
    return compteur;
}



// exercice 2



int sac_a_dos(int t, int *tab){
    for (int i = 0; i < t; i++){
        if (tab[i] > t){
            t -= tab[i];
        }
    }
    if (t == 0){
        return 1;
    }
    else{
        return 0;
    }
    
            
}


// exercice 3

int toutes_lettres_différentes(const char *s){
    int i = 0;
    while (s[i] != '\0'){
        for (int j = 0; j < i; j++){
            if (s[i] == s[j]){
                return 0;
            }
        }
        i++;
    }
    return 1;
}

int toutes_lettre_differents (char *s){
    int letre[26] ={0, 0, 0, 0, 0, 0, };
}



// test

int main() {
    // Test cexercice 1
    const char *testString = "hello world";
    int numVoyelles = compte_voyelles(testString);
    printf("Number of vowels in '%s': %d\n", testString, numVoyelles);

    // Test exercice 2
    int tab[] = {5, 4, 3, 2, 1};
    int t = 10;
    int result = sac_a_dos(t, tab);
    printf("Can the backpack be exactly filled? %s\n", result ? "Yes" : "No");

    return 0;
}