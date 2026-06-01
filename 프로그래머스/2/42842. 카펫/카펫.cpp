#include <vector>
using namespace std;

vector<int> solution(int brown, int yellow) {
    int total = brown + yellow;

    // total = x * y 이므로 약수 탐색
    for (int y = 1; y <= total; y++) {
        if (total % y != 0) continue;
        int x = total / y;

        // 갈색 테두리 조건: (x-2)*(y-2) == yellow
        if ((x - 2) * (y - 2) == yellow)
            return {x, y};
    }
    return {};
}