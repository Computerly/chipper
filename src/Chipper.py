import os
# import pygame for sound player
#from pygame import mixer

# Disable pygame printing
#! TODO Better approach is to edit pygame __init__.py !#
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

class Chipper:
	"""	docstring for Chipper
		Chipper handles music methods

		Example RFID
		7a313b4c - 2 tracks -> 297759461663
		2537bf43 - 1 track
		70159ba2 - 1 track
		f7ffe896 - 1 track
		dab67767 - 1 track
		f14d62ef - 1 track
		e5c29e22 - 1 track
		555f044e - 1 track
		23a10515 - 1 track
		7bdf1b9c - 1 track -> 640788189574
		9fdda860 - 1 track -> 298768126444
		6adcf2d9 - 3 tracks -> 436073124296
	
		A: 297759461663 - 2 Tracks
		B: 640788189574 - 1 Track
		C: 298768126444 - 1 Track
		D: 436073124296 - 3 Tracks

		Classical: 95679415974
		Electro: 1059043076972
		Lullaby: 36710907736
		Rock: 772261076731

	"""

	def __init__(self):
		# Media UID
		self.media_uid = 999999999999

		# Track number
		self.track_number = 0

		# pygame.mixer docs
		# https://www.pygame.org/docs/ref/mixer.html

		#pygame.mixer.music docs
		# https://www.pygame.org/docs/ref/music.html
		
		# Volume Level
		# Ranges from 0.0 - 1.0
		self.volume = 0.5
		

		# Play states
		self.PLAY_STATES = {
			"pause": 0,
			"play": 1,
			"stop": 2
		}

		# Current play state
		self.play_state = self.PLAY_STATES["stop"]

		# Init pygame
		pygame.init()
		
		# Init mixer
		pygame.mixer.init()

		# Set event
		self.TRACK_END = pygame.USEREVENT + 1
		pygame.mixer.music.set_endevent(self.TRACK_END)

	def update(self):
		#print("updating!")
		for evt in pygame.event.get():
			if evt.type == self.TRACK_END:
				self.handleTrackEnd()

	###################
	# Media Controls
	###################

	def pause(self):
		pygame.mixer.music.pause()
		self.play_state = self.PLAY_STATES["pause"]
	
	def play(self):
		if(self.play_state == self.PLAY_STATES["pause"]):
			pygame.mixer.music.unpause()
		else:
			pygame.mixer.music.play()

		self.play_state = self.PLAY_STATES["play"]
		
		print(f'Now playing "{self.media_uid}.{self.track_number:03d}"')

	def volume(self, level):
		pygame.mixer.music.set_volume(level)

	def skip(self):
		self.track_number += 1
		self.load_media()


	###################
	# Load Media
	###################

	def load_media(self, uid = None, trackNumber = None):
		# Default args
		if uid == None:
			uid = self.media_uid
		if trackNumber == None:
			trackNumber = self.track_number

		if os.path.isfile(f"tracks/{uid}.{trackNumber:03d}.mp3"):
			self.track_number = trackNumber
			self.media_uid = uid
			self.play_state = self.PLAY_STATES["play"]
			pygame.mixer.music.load(f"tracks/{self.media_uid}.{trackNumber:03d}.mp3")
			self.play()
		else:
			print(f'Track "{uid}.{trackNumber:03d}.mp3" does not exist!')

	###################
	# Track end Hook
	###################

	def handleTrackEnd(self):
		print("handleTrackEnd")
		self.track_number += 1
		if os.path.isfile(f"tracks/{self.media_uid}.{self.track_number:03d}.mp3"):
			self.load_media()
		else:
			self.track_number -= 1
			print("End of track")
