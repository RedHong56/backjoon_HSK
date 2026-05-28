#include <vector>
#include <unordered_map> 
#include <unordered_set>

using namespace std;

unordered_map<char, vector<char>> adjList; // 인접 리스트
vector<char> result;
unordered_set<char> visited;
void dfs(char node) {
  visited.insert(node);
  result.push_back(node);

  for (char rel : adjList[node]) {
    if (visited.find(rel) == visited.end()) { //방문리스트에 없으면
      dfs(rel);
    }
  }
}
vector<char> solution(vector<pair<char, char>> graph, char start) { //간선, 시작 노드
  for (auto& [u,v] : graph) // 인접 리스트 만들기
    adjList[u].push_back(v);

  dfs(start);

  return result;
}


//아래 코드는 테스트 코드 입니다.
#include <iterator>
#include <iostream>

using namespace std;


void init()
{
  adjList.clear();
  result.clear();
  visited.clear();
}
void print(vector<char> vec)
{
  copy(vec.begin(), vec.end(), std::ostream_iterator<char>(cout, " "));
  cout << endl;
    
}

int main()
{
  //bool 반환할 때 true는 1, false는 0 입니다.
  print(solution({{'A', 'B'}, {'B', 'C'}, {'C', 'D'}, {'D', 'E'}}, 'A')); //출력값 : A B C D E
  init();
  print(solution({{'A', 'B'}, {'A', 'C'}, {'B', 'D'}, {'B', 'E'}, {'C', 'F'}, {'E', 'F'}}, 'A')); //출력값 : A B D E F C

  return 0;
}
