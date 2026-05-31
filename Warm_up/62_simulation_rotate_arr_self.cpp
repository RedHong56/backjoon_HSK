#include <vector>

using namespace std;

vector<vector<int>> rotate (vector<vector<int>>& arr) {  
  int size = arr.size();
  vector<vector<int>> rotated_arr(size, vector<int>(size, 0));

  for (int i =0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      rotated_arr[j][size - i - 1] = arr[i][j] ;
    } 
  }
  return rotated_arr;
}

vector<vector<int>> solution(vector<vector<int>> arr, int n) {
  while(n != 0) {
    arr = rotate(arr);
    n--;
  }
  
  return arr;
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
  print(solution({
                   {1, 2, 3, 4},
                   {5, 6, 7, 8},
                   {9, 10, 11, 12},
                   {13, 14, 15, 16}
                 }, 1));
  /*
    출력값
    13 9 5 1 
    14 10 6 2 
    15 11 7 3 
    16 12 8 4 
  */
  
  print(solution({
                   {1, 2, 3, 4},
                   {5, 6, 7, 8},
                   {9, 10, 11, 12},
                   {13, 14, 15, 16}
                 }, 3));
  /*
    출력값
    4 8 12 16 
    3 7 11 15 
    2 6 10 14 
    1 5 9 13 
  */
             
  return 0;
}
