#include <string>
#include <vector>

using namespace std;
vector<bool> visited;
// 방문을 한게 있으면? 같은 컴포넌트인거임
void dfs(vector<vector<int>>& computers, int start) {
    visited[start] = true;
    
    for (int i = 0; i < computers[start].size(); i++) {
        if (!visited[i] && computers[start][i]) { // 방문 안했고 연결이 되있다면
            dfs(computers, i);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    visited = vector<bool>(computers.size(), false);
    
    int cnt = 0;
    
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs (computers, i);
            cnt ++;
        }
    }
    
    return cnt;
}