#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    // 수포자 삼인방 찍는 규칙 정의
    vector<int> s1 = {1,2,3,4,5};
    vector<int> s2 = {2,1,2,3,2,4,2,5};
    vector<int> s3 = {3,3,1,1,2,2,4,4,5,5};
    vector<int> students = {0, 0, 0};
    
    // 체점하기
    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == s1[i%5]) {
            students[0] += 1;
        }
        
        if (answers[i] == s2[i%8]) {
            students[1] += 1;
        }
        
        if (answers[i] == s3[i%10]) {
            students[2] += 1;
        }
    }
    
    // 가장 많이 맞은 사람을 answer에 정리
    int high_score = *max_element(students.begin(), students.end());
    for (int i = 0; i < students.size(); i++){
        if (students[i] == high_score) {
            answer.push_back(i+1);
        }
    }
    return answer;
}