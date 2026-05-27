#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
map<string,int> combi;

void combination (string src, string dst, int depth) {
    if (dst.size() == depth) 
        combi[dst]++; // hash[메뉴 갯수] ++

    else {
        for ( int i = 0; i< src.size(); i++) 
        combination(src.substr(i + 1), dst + src[i], depth);
    }
}

// 조합 문제
vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    
    for (string& order : orders)
        sort(order.begin(), order.end()); // 오름 차순 정렬
    
    for (int len: course) {
        for (string order : orders)
            combination(order, "", len); // cnt
    
        // 가장 많은 빈도 수 저장
        int maxOrder = 0;
        for (auto it: combi)
            maxOrder = max(maxOrder, it.second);

        for (auto it : combi)
            if (maxOrder >= 2 && it.second == maxOrder)
                answer.push_back(it.first);
        combi.clear();
    }
    sort(answer.begin(), answer.end());

    return answer;
}