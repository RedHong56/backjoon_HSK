/*
# 제약 조건
- arr의 길이는 2 이상 10^5 이하 => O(N^2) 불가능 if 제한 시간 3초 라면
- arr의 원 값은 - 100,000 이상 100,000 이하

# 입출력의 예
{1,-5,2,4,3} => {-5, 1, 2, 3, 4}
*/

#include <iostream>
#include <vector>
#include <algorithm> // sort

using namespace std;

// 출력을 어떻게 하지?

vector<int> solution(vector<int> arr) {
    sort(arr.begin(), arr.end());

    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return arr;
}

int main() {
    vector<int> arr_1 = {1, -5, 2, 4, 3};
    solution(arr_1);
}