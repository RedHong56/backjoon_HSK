#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> island;

bool cmp_cost(vector<int>& a, vector<int>& b){
    return a[2] < b[2];
}

int find(int a){
    if (island[a] == a) return a;
    
    island[a] = find(island[a]);
    
    return island[a];
}

void union_island(int a, int b) {
    int root_a = find(a);
    int root_b = find(b);
    
    if (root_a != root_b) {
        island[root_b] = root_a;
    }
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    island.resize(n);
    for (int i = 0; i < n; i++) island[i] = i; // 섬 만들어주기
    
    // cost로 정렬
    sort(costs.begin(), costs.end(), cmp_cost);
    
    // 같은 집합 일 떄까지
    for (auto& edge: costs) {
        int a = edge[0], b = edge[1], cost = edge[2];
        
        if (find(a) == find(b)){
            continue;
        }
        union_island(a, b);
        answer += cost;
    }
        
    return answer;
}