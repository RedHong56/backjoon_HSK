#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(string s) {
    int cnt = 0;
    int removed = 0;

    while (s != "1") {
        // 0 제거
        int pre_size = s.size();
        s.erase(remove(s.begin(), s.end(), '0'), s.end());
        int post_size = s.size();
        removed += pre_size - post_size;

        // 2진 변환
        int i = post_size;
        string next = "";
        while (i > 0) {
            next += to_string(i % 2);
            i /= 2;
        }
        reverse(next.begin(), next.end());
        s = next;

        cnt++;
    }

    return {cnt, removed};
}