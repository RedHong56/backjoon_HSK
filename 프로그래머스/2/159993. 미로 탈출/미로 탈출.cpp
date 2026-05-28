#include <string>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

bool valid_idx(const int& x, const int& y, const int& size_x, const int& size_y) {
    if (x < 0 || y < 0) return false;
    if (x >= size_x || y >= size_y) return false;
    return true;
}

int bfs(vector<string>& maps, pair<int,int> start, pair<int,int> end) {
    queue<tuple<int,int,int>> q;// 큐
    vector<vector<bool>> visited(maps.size(), vector<bool>(maps[0].size(), false)); // 방문 리스트
    vector<pair<int, int>> dir = {{0,1}, {1,0}, {-1,0}, {0,-1}};
    
    q.push({start.first, start.second, 0});
    visited[start.first][start.second] = true;
    
    while (!q.empty()) {
        auto [cx, cy, dist] = q.front();
        q.pop();
        
        for(auto& [x,y] : dir) {
            int dx, dy;
            dx = cx + x;  //튜플
            dy = cy + y;
            
            if (valid_idx(dx, dy, maps.size(), maps[0].size())) {
                if (make_pair(dx,dy) == end) return dist + 1;
                if (!visited[dx][dy] && maps[dx][dy] != 'X') {
                    q.push({dx, dy, dist + 1});
                    visited[dx][dy] = true;
                }
            }
        }
    }
    return -1; // 반환값: 최단거리, 도달 불가면 -1
}

// 최단거리, 가중치 동일 BFS
int solution(vector<string> maps) {
    int answer = 0;

    pair<int, int> start, lever, exit_;
    
    for (int i = 0; i < maps.size(); i++) {
        for (int j = 0; j < maps[0].size(); j++) {
            if (maps[i][j] == 'S') start = {i, j};
            else if (maps[i][j] == 'L') lever = {i, j};
            else if (maps[i][j] == 'E') exit_ = {i, j};
        }
    }
    
    int to_L = bfs(maps, start, lever); // 시작 지점을 start
    int to_E = bfs(maps, lever, exit_); // 시작 지점을 lever
    
    if (to_L == -1 || to_E == -1) return -1;
    return to_L + to_E;
}