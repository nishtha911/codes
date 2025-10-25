#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    string ip;
    int prefix;
    
    cout << "Enter IP address (e.g., 192.168.1.10): ";
    cin >> ip;
    cout << "Enter prefix (e.g., 24): ";
    cin >> prefix;

    unsigned int mask = (prefix == 0) ? 0 : (0xFFFFFFFF << (32 - prefix));
    vector<int> maskOctets(4);

    for(int i = 0; i < 4; i++) {
        maskOctets[i] = (mask >> (24 - 8*i)) & 255;
    }

    cout << "Subnet Mask: "
         << maskOctets[0] << "."
         << maskOctets[1] << "."
         << maskOctets[2] << "."
         << maskOctets[3] << endl;

    return 0;
}
