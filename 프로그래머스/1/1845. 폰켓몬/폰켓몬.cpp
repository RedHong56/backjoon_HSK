#include <vector>
#include <unordered_set>
using namespace std;

int solution(vector<int> nums)
{
    // 집합 풀이
    int answer = 0;
    
    unordered_set<int> s (nums.begin(), nums.end());
    
    return min (nums.size() / 2, s.size());;
}