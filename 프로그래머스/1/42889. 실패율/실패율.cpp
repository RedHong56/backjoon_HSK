#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 실패율은 내림차순, 실패율이 같다면 스테이지 번호는 오름차순 정렬
bool compare(const pair<int, double>& a, const pair<int, double>& b) {
    if (a.second != b.second) {
        return a.second > b.second;
    }
    return a.first < b.first;
}

vector<int> solution(int N, vector<int> stages) {
    // 실패율 = 스테이지 도달 && !clear / 스테이지 도달
    // 전체 스테이지 클리어 = N+1
    vector<int> answer;
    vector<int> arrive(N+2, 0); // 스테이지 도달
    vector<int> stay(N+2, 0); // not clear
    
    // 스테이지 클리어, 도달 확인
    for (size_t i = 0; i < stages.size(); i++) { 
        
        int current_stage = stages[i];
        
        stay[current_stage] += 1; // 머무르고 있는 스테이지
        
        for (size_t j = 1; j <= current_stage; j++) { 
            arrive[j] += 1;
        }
    }
    
    vector<pair<int, double>> stage_rates;
    
    for (int k = 1; k <= N; k++) {
        double rate = 0.0;
        
        if (arrive[k] != 0) {
            rate = (double)stay[k] / arrive[k];
        }
        
        stage_rates.push_back({k, rate});
    }
    
    sort(stage_rates.begin(), stage_rates.end(), compare);
    
    for (const auto& p : stage_rates) {
        answer.push_back(p.first);
    }
    
    return answer;
}