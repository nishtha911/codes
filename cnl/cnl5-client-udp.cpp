#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
using namespace std;

int main() {
    int client = socket(AF_INET, SOCK_DGRAM, 0);

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(9090);
    inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);

    sendto(client, "Hi Server!", 12, 0, (sockaddr*)&addr, sizeof(addr));

    char msg[100];
    socklen_t len = sizeof(addr);
    recvfrom(client, msg, sizeof(msg), 0, (sockaddr*)&addr, &len);
    cout << "Server says: " << msg << endl;

    close(client);
    return 0;
}
