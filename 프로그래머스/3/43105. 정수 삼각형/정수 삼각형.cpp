#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> triangle) {
    // [i+1][j or j+1] 최댓값 갱신
    int n = triangle.size();
    vector<vector<int>> dp(n, vector<int>(n, 0)); // 메모라이즈 초기화
    
    // 아래에서 올라올수있게 초기화
    for (int i = 0; i < n; i++) { 
        dp[n-1][i] = triangle[n-1][i];
    }
    // 큰 값 갱신
    for (int i = n-2; i >= 0; i--) {
        for (int j = 0; j <= i; j++) {
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]; 
        }
    }
    // 꼭대기 최댓값 리턴
    return dp[0][0];
}