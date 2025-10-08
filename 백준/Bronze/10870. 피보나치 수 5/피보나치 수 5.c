#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
    int a;
    scanf("%d", &a);
    int j=1,k=1,l;
    if ( 0<a && a<3){
    printf("1");
    }
    else if (a==0)
    {
        printf("0");
    }
    else{
    for(int i=3; i<=a; i++){
        l= j+k;
        j=k;
        k=l;
    }
    printf("%d", l);
    }
    return 0;
}
