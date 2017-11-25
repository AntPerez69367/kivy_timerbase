#!/usr/bin/python3

from kivy.app import App
# kivy.require("1.8.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.settings import SettingsWithSidebar
from settingsjson import settings_json
from blueclient import *
import time, sys
from kivy.uix.vkeyboard import VKeyboard

class RootWidget(FloatLayout):
	myBtConnection = BlueClient()
	myBtConnection.daemon = True
	myBtConnection.start()
	started = False
	def build(self):
		pass

	def start_timer(self):
		time = (self.ids.entry.text)
		surveyname = App.get_running_app().surveyname
		slidetime  = App.get_running_app().slidetime

		self.myBtConnection.send(time + "_" + surveyname + "_" + slidetime)
		self.started = not self.started

	def stop_timer(self):
		stop = '99'
		self.myBtConnection.send(stop)

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
			self.surveyname = self.config.get('example', 'surveyname')
			self.slidetime = self.config.get('example', 'slidetime')
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
			config.write()
			self.surveyname = config.get('example', 'surveyname')
			self.slidetime  = config.get('example', 'slidetime')

	TimerApp().run()
