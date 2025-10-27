#include <iostream>
#include <arpa/inet.h>
#include <netdb.h>
#include <cstring>
using namespace std;

int main() {
    string input;
    cout << "Enter Domain name or IP address: ";
    cin >> input;

    struct hostent *host;
    struct in_addr addr;

    if (inet_aton(input.c_str(), &addr)) {
        host = gethostbyaddr((const void *)&addr, sizeof(addr), AF_INET);
        if (host) {
            cout << "Domain Name: " << host->h_name << endl;
        } else {
            cout << "Lookup failed for IP!" << endl;
        }
    } 
    else {
        host = gethostbyname(input.c_str());
        if (host) {
            cout << "IP Address: " 
                 << inet_ntoa(*(struct in_addr*)host->h_addr) << endl;
        } else {
            cout << "Lookup failed for Domain!" << endl;
        }
    }

    return 0;
}
