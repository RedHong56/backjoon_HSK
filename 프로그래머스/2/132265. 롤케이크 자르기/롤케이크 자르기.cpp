#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int solution(vector<int> topping) {
    unordered_set<int> left;
    unordered_map<int, int> right;
    int answer = 0;

    for (int t : topping)
        right[t]++;

    for (int i = 0; i < topping.size(); i++) {
        // 왼쪽에 추가
        left.insert(topping[i]);

        // 오른쪽에서 제거
        right[topping[i]]--;
        if (right[topping[i]] == 0)
            right.erase(topping[i]);

        if (left.size() == right.size())
            answer++;
    }

    return answer;
}