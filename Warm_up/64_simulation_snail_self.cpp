#include <vector>

using namespace std;

vector<vector<int>> solution(int n) {
  // 나선형
  vector<vector<int>> snail_array(n, vector<int>(n, 0));
  int num = 1;
  // 행과 열의 시작과 끝 인덱스를 설정
  int start_row = 0, end_row = n - 1; 
  int start_col = 0, end_col = n - 1;

  while (start_row <=end_row && start_col <= end_col) {
    // 가장 왼쪽 위 
  }
  
}



//아래 코드는 테스트 코드 입니다.
#include <iterator>
#include <iostream>

using namespace std;

void print(vector<vector<int>> vec)
{
  for(int i = 0 ; i < vec.size(); i++){
    copy(vec[i].begin(), vec[i].end(), std::ostream_iterator<int>(cout, " "));
    cout << endl;
  }
  
}

int main()
{
    print(solution(3));
    /*
    출력값 :
    1 2 3 
    8 9 4 
    7 6 5
    */
                    
    print(solution(4));
    /*
    출력값: 
    1 2 3 4 
    12 13 14 5 
    11 16 15 6 
    10 9 8 7
    */
  return 0;
}
