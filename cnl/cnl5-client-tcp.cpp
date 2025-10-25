#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
using namespace std;

int main() {
    int client = socket(AF_INET, SOCK_STREAM, 0);

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);

    connect(client, (sockaddr*)&addr, sizeof(addr));

    write(client, "Hello Server!", 14);

    char msg[100];
    read(client, msg, sizeof(msg));
    cout << "Server says: " << msg << endl;

    close(client);
    return 0;
}
