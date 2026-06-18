#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    // 오름차순으로 정렬
    sort(d.begin(), d.end());
    int answer = 0;
    
    // 작은 값들로 확인
    for(auto &dd : d) {
        if (budget - dd == 0) {
            answer ++;
            break;
        }
        else if (budget - dd < 0) {
            continue;
        }
        else {
            answer ++;
            budget -= dd;
        }
    }
    return answer;
}