#include <queue>

using namespace std;

// 요세푸스 문제
// N 명의 사람이 원 형태로 서 있다
// 각 사람은 1~N 까지 번호표가 있다
// 임의의 숫자 K가 주어졌을 때 다음과 같이 사람을 없앤다
// 1. 1번 번호표를 가진 사람 기준 시계 방향으로 K번째 사람을 없앱니다
// 2. 없앤 사람 다음 사람을 기준으로 하고 다시 K 번째 사람을 없앱니다
// 3. 마지막에 남는 사람을 출력
int solution(int N, int K) {
    queue<int> q;

    for(int i = 1; i <= N; i++) {
        q.push(i);
    }

    while (q.size() > 1) {
        for (int i = 0; i < K-1; i++) {
            q.push(q.front());
            q.pop();
        }
        q.pop();
    }
    return q.front();
}


//아래 코드는 테스트 코드 입니다.
#include <iostream>

int main()
{
    
    cout << solution(5, 2) << endl; // 3

}
