#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
using namespace std;

int main() {
    int server = socket(AF_INET, SOCK_STREAM, 0);

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(7000);
    addr.sin_addr.s_addr = INADDR_ANY;

    bind(server, (sockaddr*)&addr, sizeof(addr));
    listen(server, 1);

    cout << "Waiting for client...\n";
    int client = accept(server, nullptr, nullptr);

    char msg[100];
    read(client, msg, sizeof(msg));
    cout << "Client: " << msg << endl;

    write(client, "Hello from Server!", 18);

    close(client);
    close(server);
}
