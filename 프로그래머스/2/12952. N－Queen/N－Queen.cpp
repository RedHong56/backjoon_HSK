#include <string>
#include <vector>

using namespace std;


// n*n 보드를 만들어 false로 초기화
vector<vector<bool>> board;
int cnt;
int board_size;

bool check(int x, int y) {
    // //열 확인 보드 사이즈만큼의 queen 갯수
    // for (int i = 0; i < board_size; i++)
    //     if (board[x][i]) return false;
    //행 확인
    for (int i = 0; i < board_size; i++)
        if (board[i][y]) return false;
    
    // 왼쪽 위 대각선
    for (int i = x - 1, j = y - 1; i >= 0 && j >= 0; i--, j--)
        if (board[i][j]) return false;

    // 오른쪽 위 대각선
    for (int i = x - 1, j = y + 1; i >= 0 && j < board_size; i--, j++)
        if (board[i][j]) return false;

    return true;
}

void queen_search (int queen) { // 좌표, 둔 quuen 갯수
    if (queen == board_size) {
        cnt += 1;
        return;
    }
    

    for (int i = 0; i < board_size; i++) { 
        if (check(queen, i)) {
            board[queen][i] = true; // 두기
            queen_search(queen + 1); // 재귀
            board[queen][i] = false; // 뺴기
        }
        continue;
    }
    
}

// 이때, 퀸 위치를 x축, y축, 퀸 중심 8방향 체크 하는 함수로 체크후 또 퀸 두기
int solution(int n) {
    board_size = n;
    board = vector<vector<bool>>(board_size, vector<bool>(board_size, false));

    queen_search(0);
    return cnt;
}