
class Controller:
	"""docstring for Controller"""
	def __init__(self, chipper, DEBUG):
		self.chipper = chipper
		self.DEBUG = DEBUG

		if not DEBUG:
			import RPi.GPIO as GPIO
			from mfrc522 import SimpleMFRC522
			self.reader = SimpleMFRC522()
		else:
			self.command_string = ''

	def read(self):
		# Read RFID reader
		# return None or uid
		if self.DEBUG:
			return self.console_read()

		id = self.reader.read_id_no_block()
		if id == None:
			id = self.reader.read_id_no_block()
		return id

	def console_read(self):
		cmd = input(">>> ")	
		return cmd