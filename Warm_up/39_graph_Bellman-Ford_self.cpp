#include <vector>
#include <limits>
#include <tuple>

using namespace std;

const int INF = numeric_limits<int>::max();

vector<int> solution(int num_vertices, vector<tuple<int, int, int>> edges, int source) {
  vector<vector<pair<int, int>>> graph(num_vertices);

  //❶ 간선정보를 활용해서 인접리스트를 생성
  for (auto& edge : edges) {
    int from, to, weight;
    tie(from, to, weight) = edge;
    graph[from].emplace_back(to, weight); // emplace_back: 인자를 받아서 벡터 내부에서 직접 생성 (복사 없음)
  }

 //❷ 현재까지 구한 최소비용을 INF로 설정(시작노드는 제외)
  vector<int> distance(num_vertices, INF);
  distance[source] = 0;

  //❸ 정점의 개수 -1 만큼 최소비용을 갱신
  for (int i = 0; i < num_vertices - 1; ++i) { //최대 N-1개의 간선을 거치기 때문
    for (int u = 0; u < num_vertices; ++u) { // 모든 노드를 출발점으로
      for (const auto& [v, weight] : graph[u]) { // u와 연결된 이웃들만
        if (distance[u] + weight < distance[v]) {
          distance[v] = distance[u] + weight;
        }
      }
    }
  }

  //❹ 음의 순환이 있는지 확인
  for (int u = 0; u < num_vertices; ++u) {
    for (const auto& [v, weight] : graph[u]) {
      if (distance[u] + weight < distance[v]) {
        return vector<int>(1, -1);
      }
    }
  }

  return distance;
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
  
  print(solution(5, {{0, 1, 4}, {0, 2, 3}, {0, 4, -6}, {1, 3, 5}, {2, 1, 2}, {3, 0, 7}, {3, 2, 4},{4, 2, 2}}, 0)); //출력값 : 0 -2 -4 3 -6
  print(solution(4, {{0, 1, 5}, {0, 2, -1}, {1, 2, 2}, {2, 3,-2}, {3, 0, 2}, {3, 1, 6}}, 0)); //출력값 : -1

  return 0;
}
