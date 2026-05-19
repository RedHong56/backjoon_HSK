#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    for (int i=0; i < str.length(); i++) {
        if (isupper(str[i])) {
            cout << (char)tolower(str[i]);
        } else {
            cout << (char)toupper(str[i]);
        }
    }
    return 0;       
}