#include <stack>
#include <string>
using namespace std;

// 'solution' 함수는 문자열 's'가 올바른 괄호 구조를 가지고 있는지 확인합니다.
// '(' 괄호가 나오면 스택에 푸시하고, ')' 괄호가 나오면 스택에서 팝합니다.
// 모든 문자를 확인한 후 스택이 비어있다면 괄호가 올바르게 닫힌 것입니다.
bool solution(string s) {
    stack<char> st;
    
    for (auto bracket: s) {
        if (bracket == '('){
            st.push('(');
        } else {
            if (st.empty()) {
                return false;
            } else {
                st.pop();
            }
        }
    }
    return st.empty();
}

//아래 코드는 테스트 코드 입니다.
#include <iostream>
int main()
{
    //(true를 출력하면 1 이고, false를 출력하면 0입니다.
    
    cout << solution("(())()") << endl;  // 1
    cout << solution("((())()") << endl; // 0 

    return 0;
}
