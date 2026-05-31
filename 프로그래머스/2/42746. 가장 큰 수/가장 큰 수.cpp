#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(string& a, string& b) { 
    return (a + b) > (b + a); //이게 킥
}

string solution(vector<int> numbers) {
    
    // string으로 하면 [0]가 가장 큰 수대로 나열 할 것
    vector<string> s_arr;
    for (int num : numbers) {
        string s_num = to_string(num);
        s_arr.push_back(s_num);
    }
    
    sort(s_arr.begin(), s_arr.end(), cmp);
    
    string answer = "";
    
    for (string s : s_arr) 
        answer += s;
    
    if (s_arr[0] == "0") return "0";
    
    return answer;
}