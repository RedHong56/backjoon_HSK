#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

// report: 신고 ID, 피신고 ID
vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer;
    // 유저별 신고 횟수 cnt = 명단 중복 방지 set
    unordered_map<string, unordered_set<string>> report_lst;
    unordered_map<string, int> recive;
    for (string s: id_list) {
        report_lst[s];
        recive[s];
    }
    
    // 파싱하고 set 채우기
    for (string desc: report) {
        stringstream ss(desc);
        string reporter, reported;
        ss >> reporter >> reported;
        report_lst[reported].insert(reporter);
    }

    // cnt
    for (string s : id_list) {
        if (report_lst[s].size() >= k) {
            for(auto i: report_lst[s]) {
                recive[i] ++;
            }
        }
    }
    for (string s: id_list) {
        answer.push_back(recive[s]);
    }
    
    return answer; // 메일 결과
}