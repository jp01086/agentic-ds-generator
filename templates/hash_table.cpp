#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<int, string> table;

    table[1] = "Alice";
    table[2] = "Bob";
    table[3] = "Charlie";

    for (auto &pair : table) {
        cout << pair.first << " : " << pair.second << endl;
    }

    return 0;
}