#include <iostream>
#include <string>
#include <stack>
using namespace std;

int solution(string s)
{
    stack<char> stk;
    // string 0~size 반복문
    for (char c : s) {
        // stack 비어있거나 || top 과 문자가 다르다면 push
        if (stk.empty()) stk.push(c);
        else {
            // stack.top 과 같다면 pop
            if (stk.top() == c) {
                stk.pop();
            } else {
                stk.push(c);
            }
        }
    }   
    // 만약 비어있다면 true 아니면 false
    return stk.empty();
}