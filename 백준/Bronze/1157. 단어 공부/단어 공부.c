#include<stdio.h>
#include<string.h>

int main(){
    char arr[1000000];
    int len, i;
    int count[26]; //알파벳 26글자

    scanf("%s" ,arr);
    len = strlen(arr);
    //대문자로 변환(통일)
    for (i=0; i<len; i++){
        if (arr[i]>='a' && arr[i]<= 'z')
        {
            arr[i] -= 32;
        }
        count[arr[i]-65]+=1;
    }

    int max = 0,index;

    for(i=0; i<26; i++){
        if (count[i] > max){
            max = count[i];
            index = i;
        }
    }

    //중복 확인
    int dup =0;
    for(i=0; i<26; i++){
        if (max == count[i]){
            dup ++;
        }
    }
    if(dup>1){
        printf("?");
    }else{
        printf("%c", index+65);
    }
    return 0;
}
//중복 확인하는 부분을 맥스를 갱신하면서 추가해주면 루프 한번에 처리할 수 있음