#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

bool isPrefix(string& num, unordered_map<string, int>& hash) {
    string prefix = "";
    
    for (char c: num) {
        prefix += c;
        
        if (hash.find(prefix) != hash.end() && prefix != num) {
            return true;
        }
    }
    return false;
}

bool solution(vector<string> phone_book) {
    unordered_map<string, int> hash;
    
    for (string num: phone_book) {
        hash[num] = 1;
    }
    // 문자 전체 == (문자전체) + remain
    for (string num: phone_book) {
        if (isPrefix(num, hash)) {
            return false;
        }
    }
    
    return true;
}