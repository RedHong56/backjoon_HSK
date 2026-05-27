#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    
    unordered_map<string, pair<string, int>> tree;
    for (int i = 0; i < enroll.size(); i++)
        tree[enroll[i]].first = referral[i];
    
    for (int i = 0; i < seller.size(); i++) {
        string cur = seller[i];
        int profit = amount[i] * 100;
        
        // 루트까지 타고 올라가기
        while (cur != "-" && profit > 0) {
            string parent = tree[cur].first;
            
            int give = profit / 10;         // 부모 10
            tree[cur].second += profit - give; // 본인 9
            
            if (parent == "-") break;
            
            profit = give;  // 다음 단계로 전달할 금액
            cur = parent;   // 한 단계 위로
        }
    }
    
    vector<int> answer;
    for (const auto& name : enroll)
        answer.push_back(tree[name].second);
    
    return answer;
}