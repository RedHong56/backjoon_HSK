#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    // 메모라이즈 배열 만들기 n은 2 이상 100,000 이하인 자연수
    vector<int> arr = {0, 1};
    
    for (int i = 2; i <= n; i++) {
        // 활용되는 점화식 : n = n-2 + n-1
        arr.push_back((arr[i - 1] + arr[i - 2]) % 1234567);
    }
    
    return arr[n];
}