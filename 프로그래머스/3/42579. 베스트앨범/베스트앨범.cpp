#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

bool cmp(pair<int,int> a, pair<int,int> b){
    if (a.first == b.first) 
        return a.second < b.second;
    return a.first > b.first;
}

bool cmp_g(pair<int, pair<int,string>> a, pair<int, pair<int,string>> b){
    return a.first > b.first;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer; // genres total => max, max-1
    unordered_map<string, int> total; // 장르, play
    unordered_map<string, int> first_idx; // 장르 첫 등장 인덱스
    unordered_map<string, vector<pair<int, int>>> songs; // play, idx
    
    // for 문으로 장르별 sum과 정렬된 리스트가 필요
    for (int i = 0; i < plays.size(); i++) {
        string genre = genres[i];
        int play = plays[i];
        
        total[genre] += play;
        if (first_idx.find(genre) == first_idx.end())
            first_idx[genre] = i; // 처음 등장할 때만 저장
        songs[genre].push_back({play, i}); 
    }
    
    // best 찾기
    vector<pair<int, pair<int,string>>> sorted_total;
    
    for (auto& [genre, cnt] : total) {
        sorted_total.push_back({cnt, {first_idx[genre], genre}}); // play, genre
    }
    sort(sorted_total.begin(), sorted_total.end(), cmp_g); // 내림차순
    
    // 모든 장르 순회
    for (int i = 0; i < sorted_total.size(); i++) {
        string g = sorted_total[i].second.second;
        
        sort(songs[g].begin(), songs[g].end(), cmp);
            
        answer.push_back(songs[g][0].second);
        
        if (songs[g].size() > 1) {
            answer.push_back(songs[g][1].second);
        }
    }  
    return answer;
}