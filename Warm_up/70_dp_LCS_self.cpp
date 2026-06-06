#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 두 문자열의 LCS 길이를 계산하는 함수
int solution(string str1, string str2) {
  int m = str1.length();
  int n = str2.length();

  vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0)); // 메모이제이션

  for (int i = 1; i <= m; ++i) {
    for (int j = 1; j <= n; ++j) {
      if (str1[i - 1] == str2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      }
      else {
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  // ❻ LCS 길이 반환
  return dp[m][n];
}


//아래 코드는 테스트 코드 입니다.
#include <iostream>

using namespace std;

int main()
{
  cout << solution("ABCBDAB","BDCAB") << endl; //출력값: 4
  cout << solution("AGGTAB", "GXTXAYB") << endl; //출력값 :4
  return 0;
}
