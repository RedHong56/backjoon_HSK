#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> people, int limit) {
    sort(people.begin(), people.end());

    int answer = 0;
    int light = 0;
    int heavy = people.size() - 1;

    while (light <= heavy) {
        if (people[light] + people[heavy] <= limit) {
            light++;
        }
        heavy--;
        answer++;
    }
    return answer;
}