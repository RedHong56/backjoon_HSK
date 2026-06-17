#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> land) {
    // 정수 삼각형 처럼 행 접근
    for (int i = 1; i < land.size(); i++) {
        for (int j = 0; j < 4; j++) {
            int val = 0; // 갱신 값
            for (int k = 0; k < 4; k++) {
                // 열이 다르다면 갱신
                if (k != j) { 
                    val = max(val, land[i-1][k]);
                }
            }
            land[i][j] += val;
        }
    }
    return *max_element(land.back().begin(), land.back().end());
}
