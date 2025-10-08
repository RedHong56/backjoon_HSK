#include<stdio.h>

int main(){
    int h, m, total; 
    scanf("%d %d", &h, &m);
    
    total = 60*h + m -45;

    
    if (h==0){
        if(m<45){
            h = 23;
            m = (60-45)+m;
        
        }else{
            h = 0;
            m = m-45;
        }
        
    }else{
        h = total/60;
        m = total %60;
    }

    printf("%d %d",h,m);

    return 0;
}