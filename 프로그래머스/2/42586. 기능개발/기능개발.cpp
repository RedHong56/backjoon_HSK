#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<pair<int, int>> q;
    
    for (int i = 0; i < progresses.size(); i++) {
        q.push({progresses[i], speeds[i]});
    }
    
    // 하루마다 스피드 추가
    while (!q.empty()) {
        
        for (int i = 0; i < q.size(); i++) {
            auto [prog, speed] = q.front();
            q.pop();
            q.push({prog+speed, speed});
        }
        
        // 100% 갯수 세고 answer에 추가
        int ans = 0;
        while (!q.empty() && q.front().first >= 100) {
            q.pop();
            ans += 1;
        }
        
        if (ans > 0) {
            answer.push_back(ans);
        }
    }
    return answer;
}