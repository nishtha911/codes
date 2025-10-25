#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
using namespace std;

int main() {
    int server = socket(AF_INET, SOCK_DGRAM, 0);

    sockaddr_in addr{}, client{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(9090);
    addr.sin_addr.s_addr = INADDR_ANY;

    bind(server, (sockaddr*)&addr, sizeof(addr));

    char msg[100];
    socklen_t len = sizeof(client);

    recvfrom(server, msg, sizeof(msg), 0, (sockaddr*)&client, &len);
    cout << "Client says: " << msg << endl;

    sendto(server, "Hello UDP Client", 17, 0, (sockaddr*)&client, len);

    close(server);
    return 0;
}
