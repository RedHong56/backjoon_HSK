#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

// 선수 100,000 = 시간 제한
string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> player;
    
    // 테이블 생성
    for (string p : participant) player[p] += 1;
    
    // 동명이인 같은 키 값
    for (string p : completion) {
        player[p] -= 1;
        if (player[p] == 0) {
            player.erase(player.find(p));
        }        
    }
    return player.begin()->first;
}