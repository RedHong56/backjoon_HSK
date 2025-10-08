#include<stdio.h>
#include<string.h>
#include<stdlib.h>


int facto(int a){
    if (a<=1){
        return 1;
    }
    return a*facto(a-1);
}


int main(){
    int a;
    scanf("%d", &a);
    printf("%d", facto(a));
    return 0;
}
