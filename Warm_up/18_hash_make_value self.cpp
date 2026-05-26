#include <vector>

using namespace std;
// arr 에서 target 찾기

void mapping(vector<int> &hash, const vector<int> &arr, int target) {
    for (int i=0; i< arr.size(); i++) {
        if (arr[i] > target) {
            continue;
        }
        hash[arr[i]] = 1;
    }
}

// target = arr[a] + arr[b] 찾기
// O(n^2) 은 for문 두개
// 해시를 활용해 개선하기
// 하나를 가지고 target - a = b => hash[b] 찾기 O(N)
bool solution(vector<int> arr, int target) {
    vector<int> hash(target+1, 0); // 계수 정렬
    mapping(hash, arr, target); // hash table 생성

    for (int i = 0; i < arr.size(); i++) {
        int num = target - arr[i];

        if (arr[i] == num || num < 0)
            continue;
        if (hash[num])
            return true;
    }
    return false; 
}

//아래 코드는 테스트 코드 입니다.
#include <iostream>

int main()
{
    //true를 출력하면 1이되고 false를 출력하면 0
    cout<< solution({1, 2, 3, 4, 8}, 6) << endl; // 1
    cout<< solution({2, 3, 5,9}, 10) << endl; // 0
    return 0;

}
