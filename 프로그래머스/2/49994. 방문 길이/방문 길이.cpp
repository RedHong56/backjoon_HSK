#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

int solution(string dirs) {
    map<char, pair<int,int>> cmd = {
        {'U', {0, 1}}, {'D', {0, -1}},
        {'R', {1, 0}}, {'L', {-1, 0}}
    };
    // 현재 위치 선언
    pair<int,int> cur = {0, 0};
    // set로 중복 이동 좌표 담기
    set<set<pair<int,int>>> paths;

    for (char dir : dirs) {
        auto [dx, dy] = cmd[dir];
        int nx = cur.first + dx;
        int ny = cur.second + dy;

        if (nx < -5 || nx > 5 || ny < -5 || ny > 5) {
            continue; // 범위 체크
        }

        paths.insert({cur, {nx, ny}});  // 양방향 처리
        cur = {nx, ny};
    }
    // 이동 좌표 element 수 출력
    return paths.size();
}