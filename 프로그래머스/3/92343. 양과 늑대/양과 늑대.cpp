#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int max_sheep;

void dfs(int node, vector<int> candidates, int sheep, int wolf, const vector<vector<int>>& map, const vector<int>& info) {
    
    if (!info[node]) sheep++;
    else wolf++;
    
    max_sheep = max(max_sheep, sheep);
    
    // 현재 노드 candidates에서 제거
    candidates.erase(find(candidates.begin(), candidates.end(), node));
    
    // 현재 노드의 자식들 candidates에 추가
    for (int i = 0; i < map[node].size(); i++) {
        if (map[node][i]) candidates.push_back(i);
    }
    
    // 후보들 중 갈 수 있는 곳 탐색
    for (int next : candidates) {
        if (info[next]) { // 늑대라면
            if (sheep > wolf + 1) dfs(next, candidates, sheep, wolf, map, info);
        } else { // 양이라면
            dfs(next, candidates, sheep, wolf, map, info);
        }
    }
}

int solution(vector<int> info, vector<vector<int>> edges) {
    int n = info.size();
    max_sheep = 0;
    vector<vector<int>> map(n, vector<int>(n, 0));
    
    for (int i = 0; i < edges.size(); i++) {
        int s = edges[i][0];
        int e = edges[i][1];
        map[s][e] = 1;
    }
    
    vector<int> candidates = {0};
    dfs(0, candidates, 0, 0, map, info);
    
    return max_sheep;
}