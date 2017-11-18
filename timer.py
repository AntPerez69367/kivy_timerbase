from kivy.app import App
# kivy.require("1.8.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.settings import SettingsWithSidebar
from settingsjson import settings_json
import bluetooth

class btConnection():
	import socket
	def __init__(self):
		serverMACAddress = 'B8:27:EB:C2:A4:E0'
		port = 3
		client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

	def connect(self):
		while not connection_status:
			try:
				self.client_socket.connect((self.serverMACAddress, self.port))
			except Exception as e:
				pass

	def connection_status(self):
		try:
			self.client_sock.getpeername()
			return True
		except:
			return False
		pass

	def send_data(self, data):
		self.client_socket.send(data)
		pass

	def close_connection(self):
		self.client_socket.close()
		pass


class RootWidget(FloatLayout):
	myBtConnection = btConnection()
	myBtConnection.connect()
	def build(self):
		pass

	def build_timer_data(self):
		time = (self.ids.entry.text).split(':')
		#survey_name = get survey name from settings
		#slide_time = get slide time from settings
		pass

	def start_timer(self, data):
		time = (self.ids.entry.text).split(':')
		print(time)
		#try:
		#	self.myBtConnection.send_data(time)
		#except Exception as e:
	#		raise e
	#	finally:
	#		pass
		pass

	def stop_timer(self, arg1):
		stop = '99:99:99'

		#try:
		#	self.myBtConnection.send_data(stop)
		#except Exception as e:
		#	raise e
		#finally:
		#	pass
		print(stop)

	def add_number(self, digit):
		text = self.ids.entry.text
		#print(len(text)) // for debug purposes
		if (len(text) < 8):
			if (len(text) % 3 == 2):
				if (int(digit) <= 5):
					text += ':' + digit
				else:
					pass
			else:
				text+= digit
		else:
			pass
		self.ids.entry.text = text


if __name__ == '__main__':
	class TimerApp(App):
		def build(self):
			self.use_kivy_settings = False
			self.settings_cls = SettingsWithSidebar
			return RootWidget()
		def build_config(self, config):
			config.setdefaults('example', {
							   'enablesurvey': True,
							   'surveyname': 'MySurvey',
							   'slidetime': 60 })

		def build_settings(self, settings):
			settings.add_json_panel('Settings',
									self.config,
									data=settings_json)

		def on_config_change(self, config, section, key, value):
			# re-build timer data
			pass

	TimerApp().run()
