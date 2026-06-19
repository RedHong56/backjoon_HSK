#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int solution(int k, vector<int> tangerine) {
    unordered_map<int, int> box;

    for (auto& each : tangerine)
        box[each]++;

    vector<int> sorted_cnt;
    for (auto& each : box)
        sorted_cnt.push_back(each.second);

    sort(sorted_cnt.rbegin(), sorted_cnt.rend());

    int count_sum = 0;
    int num_types = 0;
    for (int count : sorted_cnt) {   
        count_sum += count;
        num_types++;

        if (count_sum >= k) {
            break;
        }
    }
    return num_types;
}