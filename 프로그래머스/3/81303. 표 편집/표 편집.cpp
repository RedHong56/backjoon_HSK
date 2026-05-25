#include <string>
#include <vector>
#include <stack>

using namespace std;
 
// n 행 갯수 / k 행 초기 위치 / cmd 이동,수정 명령
string solution(int n, int k, vector<string> cmd) {
    string answer(n, 'O');
    stack<int> history;
    
    vector<int> up; // 앞 인덱스 값
    vector<int> down; // 뒷 인덱스 값
    
    for (int i = 0; i < n + 2; i++) { // 범퍼를 위한 +2 
        up.push_back(i - 1); // -1 ~ last idx - 1
        down.push_back(i + 1); // 1 ~ last idx + 1
    }
    k++; // 범퍼에 맞춰 + 1
    
    for (string c : cmd) {
        char action = c[0];
        
        if (action == 'C') {
            history.push(k);
            down[up[k]] = down[k];
            up[down[k]] = up[k];
            
            // 테이블 끝 계산
            if (down[k] == n + 1) k = up[k];
            else k = down[k];     
        } else if (action == 'Z') {
            int r = history.top();
            down[up[r]] = r;
            up[down[r]] = r;
            history.pop();
        } else { // 행 선택 행위
            // int size = c[2] - '0'; // 0< X 범위 < row
            int size = stoi(c.substr(2)); 
            if (action == 'U') {
                for (int j = 0; j < size; j++) k = up[k];
            } else {
                for (int j = 0; j < size; j++) k = down[k];
            }
         }
    }
    while (!history.empty()) {
        answer[history.top() - 1] = 'X';
        history.pop();
    }
    return answer;
}