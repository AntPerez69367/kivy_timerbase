from kivy.app import App
# kivy.require("1.8.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.settings import SettingsWithSidebar
from settingsjson import settings_json
from bluetooth import *
import threading, time, sys

class BlueClient(threading.Thread):
	def run(self):
		addr = 'B8:27:EB:C2:A4:E0'
		# search for the timer display service
		uuid = "00001101-0000-1000-8000-00805f9b34fb"
		service_matches = find_service( uuid = uuid, address = addr )

		while len(service_matches) == 0:
			print("Couldn't find the Timer Display =(")
			service_matches = find_service( uuid = uuid, address = addr )
			time.sleep(3)

		first_match = service_matches[0]
		port = first_match["port"]
		name = first_match["name"]
		host = first_match["host"]

		print("connecting to \"%s\" on %s" % (name, host))
		# Create the client socket
		sock=BluetoothSocket( RFCOMM )
		sock.connect((host, port))

		print("Connected")

	def close_sock(self):
		self.sock.close()


class RootWidget(FloatLayout):
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
		myBtConnection = BlueClient()
		myBtConnection.daemon = True
		myBtConnection.start()

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
