#include <string>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

int dfs(int node, int parent, const vector<vector<int>>& graph) {
    int cnt = 1;
    
    for (int child : graph[node]) {
        
        if (child != parent) {
            cnt+= dfs(child, node, graph);
        }
    }
    return cnt;
}

int solution(int n, vector<vector<int>> wires) {
    vector<vector<int>> graph(n+1);
    
    for (auto& wire: wires) { 
        int from = wire[0], to = wire[1];
        graph[from].push_back(to);
        graph[to].push_back(from); // 양방향
    }
    // 선 하나 제거 하고 카운트
    
    int min_diff = INT_MAX; // 두 컴포넌트의 최소 차이 값
    for (auto &wire : wires) {
        int a = wire[0], b = wire[1]; 
        
        graph[a].erase(remove(graph[a].begin(), graph[a].end(), b), graph[a].end());
        graph[b].erase(remove(graph[b].begin(), graph[b].end(), a), graph[b].end());
        
        int cnt_a = dfs(a, b, graph);
        int cnt_b = n - cnt_a;
        
        min_diff = min(min_diff, abs(cnt_a - cnt_b));
        
        // 삭제 전선 복구
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    return min_diff;
}