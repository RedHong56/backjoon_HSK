#include <iostream>
using namespace std;

int solution(int n) {
    int ans = 0;
    while (n > 0) {
        if (n % 2 == 1) {
            ans++;   // 홀수면 점프 한 번
            n--;
        }
        n /= 2;      // 짝수면 순간이동
    }
    return ans;
}