#include<stdio.h>
#include<string.h>

int main(){
    int tc;
    int n;
    char s[21];
    scanf("%d", &tc);

    for(int i=0; i<tc; i++){
        scanf("%d %s",&n, s);
        // printf("%d\n%s\n",n, s);
        for(int j =0; j<strlen(s); j++){
            for(int k=0; k<n; k++){
                printf("%c",s[j]);
            }
        }
        if(i<tc-1){
            printf("\n");
        }
    }
    return 0;
}


// scanf("%d %20s", …) : 입력 시 버퍼 오버플로우 방지

// strlen()을 루프 전에 계산 → 성능 개선

// putchar()를 사용해 단일 문자 출력 시 더 간결

// 입력 실패를 체크해 예외 처리

// 변수명과 주석을 붙여 가독성 향상