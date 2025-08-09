# 7/7/2024
# A Reference for the functions being called in Main.py.

import math
import os
from pytube import YouTube
import music_tag
from PIL import Image

def show_status(current, list_length):
	# Uses time to show a status bar for all threads every 1 min.
	# Current is the current item in the thread's list, list_length is
	# the length of the thread's list
	
	function_name = "show_status"
	
	try:
		# Calcualtes what percentage is done for current thread and returns
		# it as a string.
		percentage = math.trunc((current / list_length) * 100)
		percentage = str(percentage) + "%"
		return percentage
		
	except Exception as e:
		error_tracker(e, function_name)

	

def mp3ify(name, the_link, location_file):
	# mp3ify downloads the audio directly off youtube
	
	function_name = "mp3ify"
	try:
		# Converts it to a string
		name = str(name)
		the_link = str(the_link)
		location_file = str(location_file)
		
		# Downloads the mp3
		yt = YouTube(the_link)
		stream = yt.streams.get_by_itag(139)
		name = name + ".mp3"
		stream.download(output_path=location_file, filename=name)
	
	except Exception as e:
		error_tracker(e, function_name)
	

def track_record(name, filename_and_path, artist, album, track, art_path):
	# to add metadata to the mp3 file.
	
	function_name = "track_record"
	try:
		audio_file = music_tag.load_file(filename_and_path)
		audio_file['title'] = name
		
		if (artist != "Pass"):
			audio_file['artist'] = artist
			
		if (album != "Pass"):
			audio_file['album'] = album
			
		if (track != "Pass"):
			audio_file['tracknumber'] = track

		art_path = str(art_path)

		# Adds cover art for the file.
		with open(art_path , 'rb') as img_in:
			audio_file['artwork'] = img_in.read()

		# Adds a thumbnail for the audio
		art = audio_file['artwork']
		art.first.thumbnail([64, 64])
		art.first.raw_thumbnail([64, 64])
		
		# Saves the file data for the audio file
		audio_file.save()
	
	except Exception as e:
		error_tracker(e, function_name)
	
def reorganizer(file_path):
	# Creates a bunch of directories for all music.
	
	file_path = "Music/" + file_path
	
	# Makes a new folder insde the Music folder for each individual folder
	os.system("mkdir " + file_path)
	
	
	
def error_tracker(e, function_name):
	# Meant to save any errors to an external file to be saved later.
	
	error_filepath = "error.txt"
	print(function_name)
	print(e)
