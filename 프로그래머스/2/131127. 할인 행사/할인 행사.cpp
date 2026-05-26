#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

bool match(const vector<string>& dc, unordered_map<string, int> cart){
    for (string s: dc) {
        if (cart.find(s) != cart.end()) {
            cart[s]--;
            
            if (cart[s] == 0) cart.erase(s);
        }
    }
    
    if (cart.empty()) return true;
    
    return false;
}

// want를 장바구니라고 생각하고 hash로 제거 만약 0이 되면 erase 하는 형태로 구현
int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    unordered_map<string, int> cart;
    for (int i = 0; i < want.size(); i++) cart[want[i]] = number[i]; // map에 장바구니 담기
    
    for(int i = 0; i < discount.size()-9 ; i++) {
        if (match(vector<string> (discount.begin() + i, discount.begin() + i + 10), cart)) {
            answer ++;
            continue;
        }
    }
    return answer; // 14일 중 10일 겹치는걸 확인 0~9, 1~10, 2~11 ...
}