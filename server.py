import asyncio
import threading
from socket import socket

class Player:
    def __init__(self, position, current_weapon, rotation, health):
        self.Position = position
        self.CurrentWeapon = current_weapon
        self.Rotation = rotation
        self.Health = health

class Building:
    def __init__(self, position, type, health):
        self.Position = position
        self.type = type
        self.health = health

class Bullet:
    def __init__(self, position, caliber, speed):
        self.Position = position
        self.caliber = caliber
        self.speed = speed

# Define the WebSocket server as a class
class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.s = socket()
        self.s.bind(('127.0.0.1', port))
        self.s.listen(5)

        self.clients = []
        self.players = []


        print("socket is listening")
        return

    def handle_client(self, client_socket, client_id):
        # This function will handle data exchange with a single client
        while True:
            try:
                # Receive data from the client
                data_raw = client_socket.recv(1024)  # 1024 is the buffer size
                if not data_raw:
                    # If no data is received, the client has disconnected
                    break

                data = data_raw.decode()

                positions = data.split(";")

                try:
                    if len(positions) >= 2:
                        posX = int(positions[0][2:])
                        posY = int(positions[1][2:])

                        self.players[client_id].Position = [posX, posY]

                        response = "No other players"

                        for i, player in enumerate(self.players):
                            if i != client_id:
                                response = f"X={player.Position[0]};Y={player.Position[1]};ID={i};"

                        print(f"Player num: {len(self.players)}")
                        print(f"Client position: {posX},{posY}")

                        client_socket.send(response.encode())

                except:
                    print("oof")
                # Process the data and send a response back to the client

            except Exception as e:
                print(f"Error: {e}")
                break

        # Close the connection if the client disconnects
        print("Closing connection...")
        self.players.remove(client_id)
        client_socket.close()
    def update_server(self):
        # Establish connection with client.
        c, addr = self.s.accept()

        if c not in self.clients:
            print('Got connection from', addr)

            # send a thank you message to the client. encoding to send byte type.
            c.send('Thank you for connecting'.encode())

            self.clients.append(c)
            self.players.append(Player([0,0], 0, 0, 100))
            # Create a new thread to handle this client separately
            client_thread = threading.Thread(target=self.handle_client, args=(c,len(self.clients)-1))
            client_thread.start()


# Start the servers
def start_server(port):
    server = Server("", 12345)
    return server

server = start_server(34)

while True:
    server.update_server()