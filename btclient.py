from bluetooth import *
import sys

if sys.version < '3':
    input = raw_input

addr = 'B8:27:EB:C2:A4:E0'

if len(sys.argv) < 2:
    print("no device specified.  Searching all nearby bluetooth devices for")
    print("the SampleServer service")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on %s" % addr)

# search for the timer display service
uuid = "00001101-0000-1000-8000-00805f9b34fb"
service_matches = find_service( uuid = uuid, address = addr )

while len(service_matches) == 0:
    print("Couldn't find the Timer Display =(")
    service_matches = find_service( uuid = uuid, address = addr )

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))

print("Connected")
while True:
    data = input()
    if len(data) == 0: break
    sock.send(data.encode())

sock.close()
