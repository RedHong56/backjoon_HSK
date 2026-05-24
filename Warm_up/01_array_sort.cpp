#include <vector>
#include <algorithm> //sort를 위해 선언

using namespace std;

vector<int> solution(vector<int> arr) {
    sort(arr.begin(), arr.end()); // 오름 차순
    // sort(arr.rbegin(), arr.rend()); // 내림차순
    return arr;
}


//아래 코드는 테스트 코드 입니다.

#include <iterator>
#include <iostream>
void print(vector<int> vec)
{
    copy(vec.begin(), vec.end(), std::ostream_iterator<int>(cout, " ")); 
    // copy"A에서 B까지를 C로 복사해"라는 알고리즘입니다. copy(시작, 끝, 목적지);
    //ostream_iterator는 이 = (대입 연산자)의 실제 동작을 cout <<으로 바꿔놓은 특수한 객체
    /*"출력 스트림을 목적지처럼 쓸 수 있게 해주는 어댑터" 입니다.

    copy는 원래 "메모리 → 메모리" 복사인데,

    ostream_iterator를 쓰면 "메모리 → 화면 출력"으로 바꿔줍니다.

    ostream_iterator를 쓰면 중간 메모리 복사 없이 바로 출력합니다.
    ostream_iterator<int>(cout, " ")
    //                     ↑       ↑
    //               출력 대상   구분자*/

    cout << endl;
}

int main()
{
    print(solution({1, -5, 2, 4, 3}));      // -5 1 2 3 4 
    print(solution({2, 1, 1, 3, 2, 5, 4})); // 1 1 2 2 3 4 5 
    print(solution({6, 1, 7}));             // 1 6 7 
    
    return 0;
}
