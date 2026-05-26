#include <string>
#include <vector>
#include <queue>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    string answer = "No";
    queue<string> deck1, deck2;
    
    for (string s: cards1) deck1.push(s);
    for (string s: cards2) deck2.push(s);
    
    for (string target : goal) {
        // 각 덱에서 확인
        if (!deck1.empty() && target == deck1.front()) {
            deck1.pop();
            continue;
        } else if (!deck2.empty() && target == deck2.front()) {
            deck2.pop();
            continue;
        } else { // 없을 때
            return answer;
        }
    }
    answer = "Yes";
    return answer;
}