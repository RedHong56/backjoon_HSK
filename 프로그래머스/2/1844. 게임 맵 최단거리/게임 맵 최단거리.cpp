#include<vector>
#include<queue>
using namespace std;
int n, m, cnt;
struct point {
    int x,y,cnt;
};
vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};
vector<vector<bool>> visited;
queue<point> q;
bool valid (int x, int y) {
    if (x < 0 || y < 0 || x >= n || y >= m)
        return false;
    return true;
}

int bfs (vector<vector<int>> maps) {
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    q.push({0,0,1});
    visited[0][0] = true;
    
    while (!q.empty()) {
        point cur = q.front();
        q.pop();
        
        for (int i = 0; i < 4; i++) { // 4방향
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];
            
            if (valid(nx, ny)){
                if (nx == n-1 && ny == m-1) return cur.cnt + 1;
                
                if(!visited[nx][ny] && maps[nx][ny]) {
                   q.push({nx, ny, cur.cnt +1});
                   visited[nx][ny] = true;
               }
            }
        }
    }
    return -1;
}

int solution(vector<vector<int>> maps)
{   n = maps.size();
    m = maps[0].size();
 
    for (int i; i < n; i++)
        for (int j; j < n; j++)
            if(maps[i][j] == 1) cnt ++; // 총 갯수 파악
 
    return bfs(maps);
}