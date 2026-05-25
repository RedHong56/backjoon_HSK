#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    stack<int> stk; //뽑기 보관함
    unsigned size = board.size();
    
    // 하지만 move = column 단위인데 메모리 괜찮나?
    for (int col: moves) {
        col -= 1; // index 조정
        int merchandise = 0;
        
        // 뽑을 column 존재 확인 
        for (int i = 0; i < size; i++){
            if (board[i][col] != 0){
                merchandise = board[i][col];
                board[i][col] = 0; //뽑고나면 0처리 해야지
                break;
            }
        }
            
        // 보관함 영역
        if(merchandise){
            // cout << merchandise << endl;
            if(stk.empty()){
                stk.push(merchandise);
            } else {
                if (merchandise == stk.top()) {
                    stk.pop();
                    answer += 2;
                } else{
                    stk.push(merchandise);
                }

            }
        }
    }
    return answer;
}