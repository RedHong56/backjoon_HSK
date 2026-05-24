#include <string>
#include <vector>
#include <algorithm> //sort, unique 사용

using namespace std;

vector<int> solution(vector<int> numbers) {
    
    vector<int> answer;
    
    // 두 수를 우선 뽑아서 더 한 값을 arr에
    for (size_t i = 0; i < numbers.size(); i ++){
        for (size_t j = i + 1; j < numbers.size(); j ++){
            answer.push_back(numbers[i] + numbers[j]);
        }
    }
    
    // arr 정렬하기
    sort(answer.begin(), answer.end());
    
    // 중복 값 제거
    answer.erase(unique(answer.begin(), answer.end()), answer.end());
    
    return answer;
}