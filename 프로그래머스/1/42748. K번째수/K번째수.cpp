#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for (vector<int> command : commands) {
        int start = command[0] -1;
        int end = command[1];
        int idx = command[2] -1;
        
        vector<int> temp(array.begin() + start, array.begin() + end); 
        sort(temp.begin(), temp.end());
        answer.push_back(temp[idx]);
    }
    
    return answer;
}