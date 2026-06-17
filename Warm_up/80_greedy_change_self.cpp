#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int amount) {
  vector<int> denominations = {100, 50, 10, 1};

  vector<int> change;
  for (int coin : denominations) {
    while (amount >= coin) {
      change.push_back(coin);
      amount -= coin;
    }
  }
  return change;
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
  print(solution(123)); //출력값 : 100 10 10 1 1 1
  print(solution(350)); //출력값 : 100 100 100 50
  
  return 0;
}
