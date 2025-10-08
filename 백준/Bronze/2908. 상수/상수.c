#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
    char a[4], b[4], i;
    scanf("%s %s", &a,&b);
    //참고 a[3] 은 널 캐릭터 0, 1 ,2
    // 수 뒤집기 해야함
    char first[4], second[4];

    for(i= 2; i>=0; i--){
        first[2-i] = a[i]; //0 2 1 1 2 0
        second[2-i] = b[i];
    }

    // printf("%s %s",first, second);

    // 뒤집은 문자열 int로 변환 atoi 사용
    int g,h;
    g = atoi(first);
    h = atoi(second);
    //비교하여 출력
    if (g>h){
        printf("%d", g);
    }
    else{
        printf("%d", h);
    }
    return 0;
}
