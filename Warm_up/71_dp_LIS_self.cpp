#include <vector>
#include <algorithm>

using namespace std;

// 최장 증가 부분 수열(LIS)의 길이를 계산하는 함수
int solution(const vector<int> nums) {
// 길이 중 최댓 값을 구하는 문제
  int n = nums.size();
 
  vector<int> dp(n, 1); // 문자열 길이에 따른 메모이제이션

  for (int i = 1; i < n; ++i) {
    for (int j = 0; j < i; ++j) {
      if (nums[i] > nums[j]) { // 더 큰 경우
        dp[i] = max(dp[i], dp[j] + 1);
      }
    }
  }

  // max_element 활용 (#algorithm)
  return *max_element(dp.begin(), dp.end());
}

//아래 코드는 테스트 코드 입니다.
#include <iostream>

using namespace std;

int main()
{
  cout << solution({1, 4, 2, 3, 1, 5, 7, 3}) << endl; //출력값 : 5
  cout << solution({3, 2, 1}) << endl; //출력값 : 1
  
  return 0;
}
