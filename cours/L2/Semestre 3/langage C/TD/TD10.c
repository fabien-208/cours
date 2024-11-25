# include <stdio.h>
# include <string.h>


float copier_un_real_v1(float b){
    float a;
    a= b;
    return a;
}
void copier_un_real_v2(float *a, float b){
    *a = b;
}
void copier_un_real_v3(float *a, float *b){
    *a =*b;
}
void copier_un_tableau(int a[], int b[], int n){
    int i;
    for (i=0;i<n;i++) a[i] = b[i];
}




float copier_un_real_v1_sans_egal(float b){
    float a;
    memcpy(&a, &b, sizeof(float));
    return a;
}

void copier_un_real_v2_sans_egal(float *a, float b){
    memcpy(a, &b, sizeof(float));
}

void copier_un_real_v3_sans_egal(float *a, float *b){
    memcpy(a, b, sizeof(float));
}

void copier_un_tableau_sans_egal(int a[], int b[], int n){
    memcpy(a, b, n * sizeof(int));
}




int main() {
    float a, b = 5.5;
    int arr1[5] = {1, 2, 3, 4, 5};
    int arr2[5];

    // Test copier_un_real_v1
    a = copier_un_real_v1(b);
    printf("copier_un_real_v1: a = %.2f\n", a);

    // Test copier_un_real_v2
    copier_un_real_v2(&a, b);
    printf("copier_un_real_v2: a = %.2f\n", a);

    // Test copier_un_real_v3
    copier_un_real_v3(&a, &b);
    printf("copier_un_real_v3: a = %.2f\n", a);

    // Test copier_un_tableau
    copier_un_tableau(arr2, arr1, 5);
    printf("copier_un_tableau: arr2 = ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr2[i]);
    }
    printf("\n");

    // Test copier_un_real_v1_sans_egal
    a = copier_un_real_v1_sans_egal(b);
    printf("copier_un_real_v1_sans_egal: a = %.2f\n", a);

    // Test copier_un_real_v2_sans_egal
    copier_un_real_v2_sans_egal(&a, b);
    printf("copier_un_real_v2_sans_egal: a = %.2f\n", a);

    // Test copier_un_real_v3_sans_egal
    copier_un_real_v3_sans_egal(&a, &b);
    printf("copier_un_real_v3_sans_egal: a = %.2f\n", a);

    // Test copier_un_tableau_sans_egal
    copier_un_tableau_sans_egal(arr2, arr1, 5);
    printf("copier_un_tableau_sans_egal: arr2 = ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr2[i]);
    }
    printf("\n");

    return 0;
}