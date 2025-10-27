#include <iostream>
#include <fstream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
using namespace std;

int main() {
    int server = socket(AF_INET, SOCK_DGRAM, 0);

    sockaddr_in addr{}, client{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(9000);
    addr.sin_addr.s_addr = INADDR_ANY;

    bind(server, (sockaddr*)&addr, sizeof(addr));
    cout << "UDP Server ready to receive file...\n";

    ofstream fout("received_file", ios::binary);
    char buffer[1024];
    socklen_t len = sizeof(client);

    while (true) {
        int bytes = recvfrom(server, buffer, sizeof(buffer), 0,
                             (sockaddr*)&client, &len);
        if (bytes <= 0) break;

        if (string(buffer, buffer+bytes) == "END") break;

        fout.write(buffer, bytes);
    }

    cout << "File received successfully!" << endl;
    fout.close();
    close(server);
}
