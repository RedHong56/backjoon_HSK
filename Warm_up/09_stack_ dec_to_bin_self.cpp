#include <stack>
#include <string>
using namespace std;

string solution(int decimal) {

    stack<int> stack;
    
    while (decimal > 0) {
        stack.push(decimal % 2);  
        decimal /= 2;
    }

    string binary = "";
    while (!stack.empty()) {
        binary += to_string(stack.top());  
        stack.pop();
    }
    return binary;
}


//아래 코드는 테스트 코드 입니다.
#include <iostream>
int main()
{
    cout << solution(10) << endl;       // 1010
    cout << solution(27) << endl;       // 11011 
    cout << solution(12345) << endl;    // 11000000111001 
   
    return 0;
}