import bluetooth


class ClassName(object):
    """docstring for ClassName"""
    def __init__(self):
        super(ClassName, self).__init__()
        hostMACAddress = 'B8:27:EB:C2:A4:E0' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
        port = 3
        backlog = 1
        size = 1024
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        print("binding")
        s.bind((hostMACAddress, port))
        print("listening")
        s.listen(backlog)

        while True:
            try:
                client, clientInfo = s.accept()
                print("client accepted")
                while 1:
                    data = client.recv(size)
                    if data:
                        print(data)
                        client.send(data) # Echo back to client
            except:
                print("Closing socket")
                client.close()
                s.close()


if __name__ == '__main__':
    ClassName().run()
