#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
using namespace std;

bool cmp(pair<int, int>& a, pair<int, int>& b) {
    return a.second > b.second; // 중복 없음
}
vector<int> solution(string s) {
    vector<int> answer;
    vector<pair<int, int>> cnt(100001); // idx, cnt
    // 순서는? 많이 나온 순서로 하면 될거 같은데 = 계수 정렬
    
    string temp; // 버퍼
    for(char c: s) { //문제가 1의 자리 숫자가 아닌건?
        if (isdigit(c)) temp += c;
        else {
            if (!temp.empty()) {
                int i = stoi(temp);
                cnt[i].first = i;
                cnt[i].second += 1;
                temp.clear(); // 비우기
            }
        }
    }
    // 정렬
    sort(cnt.begin(), cnt.end(), cmp);
    
    // 결과 원소 넣기
    for (auto& [a, b] : cnt) {
        if(a != 0) answer.push_back(a);
    }
    
    return answer;
}