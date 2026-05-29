#include <iostream>
#include <vector>
using namespace std;

int INF = 1e9; // 1번 의심 : c 는 10000 이하임 OK
vector<vector<int>> graph; // 가중치 기록
vector<bool> visited;

int solution(int N, vector<vector<int>> road, int K) {
    // 초기화
    visited = vector<bool>(N+1, false);
    graph = vector<vector<int>>(N+1, vector<int>(N+1, INF));
    for (auto& r: road) {
        int from = r[0];
        int to = r[1];
        int weight = r[2];
        if (graph[from][to] > weight) { // 이게 킥임
            graph[from][to] = weight;
            graph[to][from] = weight;
        }  
    } 
    
    vector<int> dist(N+1, INF); // 방문 거리 리스트
    dist[1] = 0; // 시작 노드

    for (int i = 1; i <= N; i++) { // 이건 n-1 만큼
        int min_dist = INF;
        int cur = -1;
        
        for (int j = 1; j <= N; j++) { // dist 중 가장 작은 것 찾기 + 방문 안한것            
            if (!visited[j] && dist[j] < min_dist) {
                min_dist = dist[j];
                cur = j;
            }
        }
        if (cur == -1) break; // 갈 곳 없을 때
        visited[cur] = true;


        for (int j = 1; j <= N; j++) { //이웃
            int new_dist = dist[cur] + graph[cur][j];

            if (dist[cur] != INF && !visited[j] && graph[cur][j] != INF && dist[j] > new_dist) { // 방문, 간선, 갱신
                dist[j] = new_dist;  // 거리만 갱신
            }
        }
    }
    
    int answer = 0;
    // 거리 루프 중 k 보다 같거나 작은 것 cnt
    for (int i = 1; i <= N; i++) {  // 1번부터만 카운트
        if (dist[i] <= K) answer++;
    }
    return answer;
}