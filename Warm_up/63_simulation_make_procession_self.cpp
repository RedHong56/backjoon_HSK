#include <vector>

using namespace std;

vector<vector<int>> muliply(vector<vector<int>>& matrix1, vector<vector<int>>& matrix2) {
  vector<vector<int>> result(3, vector<int>(3, 0));

  for (int i = 0; i < 3; i++){
    for (int j = 0; j < 3; j++){
      for (int k = 0; k < 3; k++){ // k = 선택된 행
        result[i][j] += matrix1[i][k] * matrix2[k][j];
      }
    }
  }

  return result;
}

vector<vector<int>> transpose(vector<vector<int>>& matrix) {
  vector<vector<int>> result(3, vector<int>(3, 0));
  for (int i = 0; i < 3; i++){
    for (int j = 0; j < 3; j++){
      result[i][j] = matrix[j][i];
    }
  }
  return result;
}


vector<vector<int>> solution(vector<vector<int>> matrix1, vector<vector<int>>matrix2) {
  vector<vector<int>> result(3, vector<int>(3, 0));
  result = muliply(matrix1, matrix2);
  result = transpose(result);

  return result;
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
    print(solution( {
                     {1, 2, 3},
                     {4, 5, 6},
                     {7, 8, 9},
                    },
                    {
                     {9, 8, 7},
                     {6, 5, 4},
                     {3, 2, 1},
                    }
                    ));
    /*
    출력값 :
    30 84 138 
    24 69 114 
    18 54 90 
    */
                    
    print(solution( {
                     {2, 4 ,6},
                     {1, 3, 5},
                     {7, 8, 9},
                    },
                    {
                     {9, 1, 2},
                     {4, 5, 6},
                     {7, 3, 8},
                    }
                    ));
    /*
    출력값: 
    76 56 158 
    40 31 74 
    76 60 134 
    */
  return 0;
}
