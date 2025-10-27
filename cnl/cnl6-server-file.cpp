#include <iostream>
#include <fstream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
using namespace std;

int main() {
    int server = socket(AF_INET, SOCK_STREAM, 0);

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8000);
    addr.sin_addr.s_addr = INADDR_ANY;

    bind(server, (sockaddr*)&addr, sizeof(addr));
    listen(server, 1);

    cout << "Waiting for connection...\n";
    int client = accept(server, nullptr, nullptr);

    ofstream fout("received.txt", ios::binary);
    char buffer[1024];
    int bytes;

    while ((bytes = read(client, buffer, sizeof(buffer))) > 0)
        fout.write(buffer, bytes);

    cout << "File received successfully!\n";

    fout.close();
    close(client);
    close(server);
}
