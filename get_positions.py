import json
import threading
from datetime import datetime
from time import sleep
from pynput.mouse import Listener
from pfmqtt import Tx

data_list = []


def on_click(x, y, button, pressed):
	# Appends pressed and released position
	if pressed:
		# Captures data and converts it to json
		data = json.dumps({"x": x, "y": y, "timestamp": datetime.timestamp(datetime.now())})
		data_list.append(data)
		print(x, y)


class MouseMonitor:
	"""
	GreyStarFish is a class that monitors cursor clicks and provides the data for Purple Finch
	"""

	def __init__(self):
		# Declare variables
		self.run = True
		self.thread_run = True
		self.t = Tx("d6f73930-cd18-4021-b28a-1d9a3e733333/6bfc17fb-3c55-4a29-81e7-c55089134ace", "mqtt.eclipse.org", "lol")

	# Define on click
	def on_click(self, x, y, button, pressed):
		# Appends pressed and released position
		if pressed:
			# Captures data and converts it to json
			data = json.dumps({"x": x, "y": y, "timestamp": datetime.timestamp(datetime.now())})
			data_list.append(data)
			print(x, y)

	def send_thread(self):
		if self.thread_run:
			self.sending = threading.Timer(1, self.send_thread).start()
			if len(data_list) > 0:
				# self.t.send_unenc(str(data_list))
				print(data_list)
				data_list.clear()

	def run_listener(self):
		# Start a listener thread

		self.send_thread()
		listener = Listener(
			on_click=on_click
		)
		listener.start()
		# This needs to be on a specific time or something
		while self.run:
			sleep(10)  # Amount of time that the listener records the input.
			self.run = False
			# Stop listener
		listener.stop()
		self.thread_run = False
