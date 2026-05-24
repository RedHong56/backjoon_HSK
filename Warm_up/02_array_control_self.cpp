/*
배열 제어하기 : 정수 배열 lst가 주어질 때 배열의 중복값을 제거하고 배열 데이터를 ㄴ림차순으로 정렬 반환 하는 solution()함수 구현

# 제약조건
1. lst의 길이는 2이상 1,000 이하
2. lst의 원소 값은 -100,000 이상 100,000이하

입출력 예시 {4, 2, 2, 1, 3, 4} => {4, 2, 1, 3}
*/

#include <iostream>
#include <vector>
#include <algorithm> // 정렬 sort() 사용, 중복 제거 unique() 사용

using namespace std;

vector<int> solution(vector<int> lst) {
    sort(lst.rbegin(), lst.rend());
    lst.erase(unique(lst.begin(), lst.end()));
    return lst;
}

#include <iterator>
void print(vector<int> vector){
    copy(vector.begin(), vector.end(), ostream_iterator<int>(cout, " "));
}

int main() {
    vector<int> arr_1 = {4, 2, 2, 1, 3, 4};
    print(solution(arr_1));
}

/*ostream이란?
Output Stream의 줄임말로, "데이터를 내보내는 통로"입니다.


프로그램 → ostream → 화면(cout) / 파일(fstream) / 문자열(sstream)
cout이 바로 ostream 타입의 객체입니다.

ostream_iterator의 생성자

ostream_iterator<T>(stream, delimiter)
//                ↑    ↑        ↑
//              타입  출력대상  구분자(선택)
인자	타입	설명
stream	ostream&	출력할 스트림 (보통 cout)
delimiter	const char*	원소 사이에 넣을 문자열 (선택)
예시

ostream_iterator<int>(cout, " ")   // 1 2 3 
ostream_iterator<int>(cout, ", ")  // 1, 2, 3, 
ostream_iterator<int>(cout)        // 123  (구분자 없음)
ostream_iterator<string>(cout, "\n") // 줄바꿈으로 구분
정리
ostream_iterator<int>(cout, " ") 는

"int를 cout에 " " 로 구분해서 출력하는 반복자를 만들어줘"

라는 뜻

# 자주 쓰이는 경우
파일 출력 (ofstream)

#include <fstream>

ofstream file("output.txt");
copy(vec.begin(), vec.end(), ostream_iterator<int>(file, "\n"));
// 파일에 한 줄씩 저장
문자열로 변환 (ostringstream)

#include <sstream>

ostringstream oss;
copy(vec.begin(), vec.end(), ostream_iterator<int>(oss, " "));
string result = oss.str(); // "1 2 3 "
에러 출력 (cerr)

copy(vec.begin(), vec.end(), ostream_iterator<int>(cerr, " "));
// 표준 에러 스트림으로 출력
정리
스트림	목적지
cout	화면
ofstream	파일
ostringstream	문자열(메모리)
cerr	에러 화면
코딩테스트에서는 거의 cout만 쓰지만, 실무에서는 파일 저장할 때 ofstream이 자주 등장합니다.
*/