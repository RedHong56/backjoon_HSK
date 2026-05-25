#include <string>
#include <vector>
#include <stack>

using namespace std;

bool check(string brackets) {
    stack<char> st;

    for (char c : brackets) {
        if (c == '(' || c == '{' || c == '[') {
            st.push(c);
        } else {
            if (st.empty()) return false;  // 쌍 없는 닫는 괄호 → 즉시 false

            // 짝이 맞는지 확인
            char top = st.top();
            if (c == ')' && top != '(') return false;
            if (c == '}' && top != '{') return false;
            if (c == ']' && top != '[') return false;
            st.pop();
        }
    }
    return st.empty();
}

int solution(string s) {
    int answer = 0;
    
    // s 길이 만큼 반복
    for (int i = 0; i < s.size(); i++) {
        string temp = s.substr(i) + s.substr(0, i);
            
        // 회전 할 때마다 옳은 괄호인지 판별
        if (check(temp)) answer += 1;
    }
        
    return answer;
}