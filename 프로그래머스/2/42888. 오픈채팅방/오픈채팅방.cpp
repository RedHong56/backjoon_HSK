#include <string>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;
void split_blank(string& str, string& cmd, string& uid,string& name) {
    
    vector<string> tokens;
    
    size_t start = 0;
    size_t end = str.find(' ');
    
    while (end != string::npos) {
        tokens.push_back(str.substr(start, end - start));
        start = end + 1;
        end = str.find(' ', start);
    }
    tokens.push_back(str.substr(start));  
    
    cmd = tokens[0];
    uid = tokens[1];
    
    if (cmd != "Leave"){
        name = tokens[2];
    }
}

vector<string> solution(vector<string> record) {
    vector<string> answer;
    unordered_map<string, string> id_map; // uid 로 nick 찾기
    queue<pair<string, string>> q;
    
    for (string rec: record) {
        // cmd , uid, nick name 분리
        string cmd, uid, name;

        split_blank(rec, cmd, uid, name);
        // cmd에 따라서 queue로 메세지 모으기
        if (cmd == "Enter") { //cmd == enter => uid 들어왔습니다
            id_map[uid] = name;
            q.push({uid, cmd});
        } else if (cmd == "Leave") { //cmd == leave => uid 나갔습니다
            q.push({uid, cmd});
        } else { //cmd == change => map[uid] = 변경
            id_map[uid] = name;
        }
    }
    
    // 큐 빌 때까지 for문 answer에 [uid]메세지 넣기
    while(!q.empty()) {
        auto [uid, c] = q.front();
        q.pop();
        
        if (c == "Enter") answer.push_back(id_map[uid]+"님이 들어왔습니다.");
        else answer.push_back(id_map[uid]+"님이 나갔습니다.");
    }
    return answer;
}