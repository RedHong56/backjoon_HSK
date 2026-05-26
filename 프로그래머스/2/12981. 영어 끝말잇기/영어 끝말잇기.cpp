#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    unordered_map<string, int> hash;

    for (int i = 0; i < words.size(); i++) {
        string word = words[i];

        // 끝말잇기 규칙 위반 or 중복 단어
        if (i > 0 && words[i-1].back() != word.front() || hash[word]) {
            return {i % n + 1, i / n + 1};
        }
        hash[word] = 1;
    }
    return {0, 0};
}