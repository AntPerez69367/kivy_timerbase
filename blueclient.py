from bluetooth import *
import threading

class BlueClient(threading.Thread):

	def run(self):
		addr = 'B8:27:EB:C2:A4:E0'
		# search for the timer display service
		uuid = "00001101-0000-1000-8000-00805f9b34fb"
		service_matches = find_service( uuid = uuid, address = addr )
		while len(service_matches) == 0:
			try:
				print("Couldn't find the Timer Display =(")
				service_matches = find_service( uuid = uuid, address = addr )
				time.sleep(3)
			except Exception as e:
				print("Unable to connect to display.")

		first_match = service_matches[0]
		port = first_match["port"]
		name = first_match["name"]
		host = first_match["host"]

		print("connecting to \"%s\" on %s" % (name, host))
		# Create the client socket
		self.sock = self.connect(host,port)

		while True:
			data = self.sock.recv(1024).decode()
			if len(data) == 0:
				pass
			else:
				print("received [%s]" % data)

	def send(self, output):
		try:
			print("Send command received")
			self.sock.send(output.encode())
		except Exception as e:
			print("Unable to send: %s" % (output))

	def connect(self, host, port):
		connected = False
		while not connected:
			try:
				sock=BluetoothSocket( RFCOMM )
				sock.connect((host, port))
				connected = True
				App.get_running_app().root.ids.cstatus.text = 'Bluetooth Status: \nConnected'
				App.get_running_app().root.ids.cstatus.color = (0,1,0,1)
			except Exception as e:
				print("Host found. Server rejecting connection.")

		print("Connected")
		return sock

	def close_sock(self):
		self.sock.close()

