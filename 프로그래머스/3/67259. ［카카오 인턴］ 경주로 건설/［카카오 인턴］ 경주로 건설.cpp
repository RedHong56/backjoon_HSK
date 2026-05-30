#include <cstring>
#include <vector>
#include <queue>
// #include <limits>


using namespace std;

const int dx[] = {0, 0, -1, 1};
const int dy[] = {-1, 1, 0, 0};
const int S_COST = 100;
const int C_COST = 600;
const int INF = 1e9;
const int MAX_SIZE = 26;

struct Path {
    int y, x, direction;
};

bool valid(int y, int x, int size) {
    return y >= 0 && y < size && x >= 0 && x < size;
}
// 도로 건설 비용, 진행 방향, 좌표(x,y)
int solution(vector<vector<int>> board) {
    int size = static_cast<int>(board.size()); // 정사각형
    int dist[MAX_SIZE][MAX_SIZE][4]; // 좌표, 방향으로 비용 담기
    memset(dist, -1, sizeof(dist)); // memset 활용 초기화 = 고정크기
    queue<Path> q;
    
    q.push({0,0,1}); // 가로 오른칸
    q.push({0,0,3}); // 세로 아래칸
    
    dist[0][0][1] = 0;
    dist[0][0][3] = 0;
    
    while (!q.empty()) {
        auto [y, x, dir] = q. front();
        q.pop();
        
        int lastCost = dist[y][x][dir];
        
        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i], nx = x + dx[i];
            
            if (!valid(ny, nx, size) || board[ny][nx])
                continue;
            
            int newCost = lastCost + (i == dir ? S_COST : C_COST);
            // int newCost = lastCost + S_COST + (i == dir ? 0 : C_COST);
            
            if (dist[ny][nx][i] == -1 || dist[ny][nx][i] > newCost) {
                dist[ny][nx][i] = newCost;
                q.push({ny, nx, i});
            }
        }
    }
    
    int answer = INF;
    
    for (int i = 0; i < 4; i++) {
        if (dist[size-1][size-1][i] != -1) {
            answer = min(answer, dist[size-1][size-1][i]);
        }
    }
    return answer == INF ? -1 : answer;
}
    

