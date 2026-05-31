#include <string>
#include <vector>

using namespace std;

// 계수 정렬을 활용해 사전순 정렬
string solution(string s) {
  // 알파벳 = [26] = 갯수
  vector<int> v(26);
  string result = "";
  for (char c : s) {
    v[c - 'a'] ++;
  }
  
  for (int i = 0; i < 26; i++) {
    result += string(v[i], i + 'a');
  }
  
  return result;
}

//아래 코드는 테스트 코드 입니다.
#include <iostream>

using namespace std;

int main()
{
  cout << solution("hello") << endl; // 출력값 : ehllo
  cout << solution("algorithm") << endl; // 출력값 : aghilmort
  
  return 0;
}

