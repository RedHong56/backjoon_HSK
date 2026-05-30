#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> clear;
int answer;

void backtracking (int hp, int ans, vector<vector<int>>& dungeons) {
    for (int i = 0; i < dungeons.size(); i++) {
        int need = dungeons[i][0], consume = dungeons[i][1];
        // 유망 함수 조건 필요 피로도를 기준으로

        // 결과에 있는지 확인, 필요 값이 충분한지 확인
        if (find(clear.begin(), clear.end(), i) == clear.end() && hp - need >= 0){
            clear.push_back(i);
            hp -= consume;
            ans ++;
            answer = max(answer, ans);
            backtracking(hp, ans, dungeons);
            
            // 원복
            hp += consume;
            ans --;
            clear.pop_back();
        }
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    answer = 0;
    backtracking(k, answer, dungeons);
    
    return  answer;// 던전 갯수
}