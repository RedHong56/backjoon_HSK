#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

unordered_map<int, vector<int>> adjList;
vector<int> result;
unordered_set<int> visited;
queue<int> q;

void bfs (int start) {
  q.push(start);
  visited.insert(start);

  while(!q.empty()){
    int node =  q.front();
    q.pop();

    for (int rel : adjList[node]) {
      if (visited.find(rel) == visited.end()) {
        q.push(rel);
        visited.insert(rel);
        result.push_back(rel);
      }
    }
  }
}

vector<int> solution(vector<pair<int, int>> graph, int start) { // <노드 시작 , 노드 도착>
  for (auto &[u,v] : graph) // 인접리스트 생성
    adjList[u].push_back(v);

  bfs(start);

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
 
}
void print(vector<int> vec)
{
  copy(vec.begin(), vec.end(), std::ostream_iterator<int>(cout, " "));
  cout << endl;
    
}

int main()
{
  
  print(solution({{1, 2}, {1, 3}, {2, 4}, {2, 5}, {3, 6}, {3, 7}, {4, 8}, {5, 8}, {6, 9}, {7, 9}}, 1)); //출력값 : 1 2 3 4 5 6 7 8 9
  init();
  print(solution({{0, 1}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 0}}, 1)); //출력값 : 1 2 3 4 5 0
  return 0;
}
