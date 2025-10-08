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