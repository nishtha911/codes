#include <iostream>
#include <fstream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
using namespace std;

int main() {
    int client = socket(AF_INET, SOCK_DGRAM, 0);

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(9000);
    inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);

    string filename;
    cout << "Enter filename to send: ";
    cin >> filename;

    ifstream fin(filename, ios::binary);

    char buffer[1024];
    socklen_t len = sizeof(addr);

    while (fin.read(buffer, sizeof(buffer)) || fin.gcount() > 0) {
        int bytes = fin.gcount();
        sendto(client, buffer, bytes, 0, (sockaddr*)&addr, len);
    }

    sendto(client, "END", 3, 0, (sockaddr*)&addr, len);

    cout << "File sent successfully!" << endl;
    fin.close();
    close(client);
}
