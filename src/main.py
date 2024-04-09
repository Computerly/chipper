import os

from Chipper import Chipper

from Controller import Controller

DEBUG = False

if os.name == 'nt':
	os.add_dll_directory("C:/Python39/Lib/site-packages/pygame/libmpg123-0.dll")
	DEBUG = True

def main():
	if DEBUG:
		print("DEBUG ON")

	chipper = Chipper()
	app = Controller(chipper, DEBUG)
	uid = None
	#while uid == None:
	print("Loaded!")

	while True:	
		uid = app.read()
		chipper.update()
				
		if (uid == chipper.media_uid) and (chipper.play_state == chipper.PLAY_STATES["pause"]):
			chipper.play()
		elif (uid == None or uid == "no_chip") and (chipper.play_state == chipper.PLAY_STATES["play"]):
			chipper.pause()
		elif uid == None or uid == "no_chip":
			pass
		elif (uid == chipper.media_uid) and (chipper.play_state == chipper.PLAY_STATES["play"]):
			pass
		elif uid == "pause":
			chipper.pause()
		elif uid == "play":
			chipper.play()
		elif uid == "skip":
			chipper.skip()
		elif uid == "quit":
			break
		elif uid == "name":
			print(f"Playing: {chipper.media_uid}.{chipper.track_number:03d}.mp3")
		else:
			chipper.load_media(uid, 0)


		
if __name__ == '__main__':
	main()
