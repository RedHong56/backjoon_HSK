#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    // 길이 100,000 N^2 이하
    vector<int> answer(prices.size());
    stack<int> stk;
    
    // 길이를 확정한 주식은 제외하기
    for (int i = 0; i < prices.size(); i++) {  
        while(!stk.empty() && prices[stk.top()]>prices[i]){
            answer[stk.top()] = i-stk.top();
            stk.pop();
        }
        stk.push(i);
    }
    // 스택이 비어있다면
    while(!stk.empty()){
        answer[stk.top()] = prices.size()-stk.top()-1;
        stk.pop();
    }
    return answer;
}