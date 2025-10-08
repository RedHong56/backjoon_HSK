#include<stdio.h>

int main(){
    int a, max, index=1;
    for(int i=0; i<9; i++){
        scanf("%d" ,&a);
        if(i==0){
            max=a;
        }
        else{
            if (max<a)
            {
                max = a;
                index = i+1;
            }
        }
    }
    printf("%d\n%d",max,index);
    return 0;
}