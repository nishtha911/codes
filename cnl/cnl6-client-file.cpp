#include <iostream>
#include <fstream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
using namespace std;

int main() {
    int client = socket(AF_INET, SOCK_STREAM, 0);

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8000);
    inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);

    connect(client, (sockaddr*)&addr, sizeof(addr));

    ifstream fin("send.txt", ios::binary);
    char buffer[1024];
    int bytes;

    while (fin.read(buffer, sizeof(buffer)) || (bytes = fin.gcount()) > 0)
        write(client, buffer, bytes);

    cout << "File sent successfully!\n";

    fin.close();
    close(client);
}
