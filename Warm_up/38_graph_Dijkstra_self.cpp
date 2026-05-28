#include <vector>
#include <tuple>

using namespace std;

const int INF = 99999; // 파이썬과 달리 직접 명시
const int MAX_NODES = 100;
int graph[MAX_NODES][MAX_NODES]; // 인접 행렬 [출발 노드] [도착 노드] val = cost
bool visited[MAX_NODES]; // 방문 리스트

// 최소 비용, 직전 노드
vector<int> solution(int start, int numNodes, const vector<tuple<int, int, int>> edges) {
  for (int i = 0; i < MAX_NODES; ++i) {
    fill_n(graph[i], MAX_NODES, INF);
    visited[i] = false;
  }
  
  //❷ 입력받은 간선 정보를 그래프로 표현
  for (const auto& [from, to, weight] : edges) {
    graph[from][to] = weight;
  }

  //❸ 시작 노드를 제외한 모든 노드의 최소 비용을 INF로 초기화
  vector<int> distances(numNodes, INF); // 최소 비용 관리
  distances[start] = 0;

  for (int i = 0; i < numNodes - 1; ++i) {
    int minDistance = INF;
    int closestNode = -1;

    //❹ 최소 거리 노드 찾기
    for (int j = 0; j < numNodes; ++j) {
      // 방문 X 이면서 기존에 기록된 값과 새로운 min 거리 비교
      if (!visited[j] && distances[j] < minDistance) { // start는 0 < -1
        minDistance = distances[j]; // 0으로 갱신
        closestNode = j; // j = 0
      }
    }

    //❺ 찾은 노드를 방문 처리
    visited[closestNode] = true;

    //❻ 인접 노드에 대한 거리 업데이트
    for (int j = 0; j < numNodes; ++j) {
      int newDistance = distances[closestNode] + graph[closestNode][j]; // 새 거리 갱신 
      if (!visited[j] && graph[closestNode][j] != INF && newDistance < distances[j]) { //  방문 안 했고, 실제로 연결된 이웃이고, 더 짧은 경로면
        distances[j] = newDistance;
      }
    }
  }

  return distances;
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
  
  print(solution(0, 3, {{0, 1, 9},{0, 2, 3},{1, 0, 5},{2, 1, 1}})); //출력값 : 0 4 3
  print(solution(0, 4, {{0, 1, 1}, {1, 2, 5}, {2, 3, 1}})); //출력값 : 0 1 6 7
  return 0;
}
