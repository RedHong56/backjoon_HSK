#include <string>
#include <vector>

using namespace std;
// 1, 2, 3, 5, 8 ...
int solution(int n) {
    vector<int> arr = {0, 1, 2};
    if (n < 3) return n;
    else {
        for (int i = 3; i <= n; i++) {
            arr.push_back((arr[i - 1] + arr[i - 2]) % 1000000007);
        }
    }
    return arr[n]; // 경우의 수를 1,000,000,007으로 나눈 나머지를 return
}