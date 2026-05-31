#include <vector>

using namespace std;

vector<int> solution(vector<int> arr1, vector<int> arr2) {
  //정렬 완료되어 있는 정렬 => merge 정렬 처럼
  vector<int> merge;
  int i = 0, j = 0;
  // 비교하고 추가

  while (i < arr1.size() && j < arr2.size()) {
    if (arr1[i] <= arr2[j]) {
      merge.push_back(arr1[i]);
      i ++;
    } else {
      merge.push_back(arr2[j]);
      j ++;
    }
  }
  // 남은 것들 생각 안함
  while (i < arr1.size()) {
    merge.push_back(arr1[i]);
    i ++;
  }

  while (j < arr2.size()) {
    merge.push_back(arr2[j]);
    j ++;
  }
  
  return merge;
}


//아래 코드는 테스트 코드 입니다.
#include <iterator>
#include <iostream>

using namespace std;

void print(vector<int> vec)
{
  copy(vec.begin(), vec.end(), std::ostream_iterator<int>(cout, " "));
  cout << endl;
}

int main()
{
  print(solution({1, 3, 5}, {2, 4, 6})); // 출력값 : 1 2 3 4 5 6
  print(solution({1, 2, 3}, {4, 5, 6})); // 출력값 : 1 2 3 4 5 6
  
  return 0;
}

