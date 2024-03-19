import socket
import eiscp
import eiscp.core
import socketserver
import threading

class OnkyoServer:

    class Handler(socketserver.StreamRequestHandler):
        def handle(self):
            # self.request is the TCP socket connected to the client
            self.data = self.request.recv(1024).strip()
            print("Received from {}:".format(self.client_address[0]))
            print(self.data)
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())

    def __init__(self):
        self.broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.broadcast_socket.bind(('0.0.0.0', eiscp.eISCP.ONKYO_PORT))

        self.server_socket = socketserver.ThreadingTCPServer(('0.0.0.0', eiscp.eISCP.ONKYO_PORT), OnkyoServer.Handler)
        server_thread = threading.Thread(target=self.server_socket.serve_forever)
        server_thread.daemon = True
        server_thread.start()




    def loop(self):
        while True:
            data, addr = self.broadcast_socket.recvfrom(1024)
            packet = eiscp.core.eISCPPacket.parse(data).strip()
            print(f'Received: {packet} from {addr}')
            magic_onkyo = '!xECNQSTN'
            magic_pioneer = '!pECNQSTN'
            print(f'Compare to: {magic_onkyo}/{magic_pioneer}')
            if packet == magic_onkyo or packet == magic_pioneer:
                response = eiscp.core.eISCPPacket("!1ECNTX-NR7100/60128/DX/0009B060B053")
                print(f"Sending back {response}")
                self.broadcast_socket.sendto(response.get_raw(), addr)
            else:
                print(f'{packet} != {magic_onkyo} or {magic_pioneer}')

def main():
    e = eiscp.eISCP("10.10.10.246")
    print(e.info)
    server = OnkyoServer()
    server.loop()

main()
    # info = re.match(r'''
    #     !
    #     (?P<device_category>\d)
    #     ECN
    #     (?P<model_name>[^/]*)/
    #     (?P<iscp_port>\d{5})/
    #     (?P<area_code>\w{2})/
    #     (?P<identifier>.{0,12})
    # ''', response.strip(), re.VERBOSE).groupdict()


