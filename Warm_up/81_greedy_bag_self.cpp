#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

bool sort_val(vector<double>& a, vector<double>& b){
  return a[2] > b[2];
}

// 무게, 가치 
double solution(vector<vector<double>> items, double weight_limit) {
  // 무게당 가치를 벡터에 추가
  for (auto &item : items)
    item.push_back(item[1] / item[0]);
  // 가치/무게 정렬
  sort(items.begin(), items.end(), sort_val);

  double total_value = 0;

  for (const auto &item : items) {
    if (item[0] <= weight_limit) {
      total_value += item[1];
      weight_limit -= item[0];
    } else {
      double fraction = weight_limit / item[0];
      total_value += item[1] * fraction;
      break;
    }
  }

  return total_value;// 가치 최대 수용
}

//아래 코드는 테스트 코드 입니다.
#include <iostream>

int main()
{
  cout << solution({{10, 19}, {7, 10}, {6, 10}}, 15) << endl; //출력값 : 27.3333
  cout << solution({{10, 60}, {20, 100}, {30, 120}}, 50) << endl; //출력값 : 240
  
  return 0;
}
