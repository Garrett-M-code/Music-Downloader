# 7/7/2024
# A Program to download and convert Youtube videos into mp3 files

from threading import Thread
import time
import Functions as pirate
from ODSReader import ODSReader

# Opens the file
document = ODSReader(u'list.ods', clonespannedcolumns=True)

# Adds document data as a nested list. Rows First, Collumns Second.
table = document.getSheet(u'Sheet1')

# Is used for display the status with a timer
global current_status
current_status = 0

# Length of the table
len_table = len(table)

##########################################################

def thread_ripper(combined):
	# Runs the completion loop for each individual item.
	
	function_name = "thread_ripper"
	
	try:
		song = combined[0]
		current_status = combined[1]
		
		song_name = song[0]
		link_url = song[1]
		song_filepath = song[2]
		song_artist = song[3]
		song_album = song[4]
		song_track = song[5]
		song_art_path = song[6]
		
		# Defines import variables to be used with the different functions
		pirate.video_query(song_name, link_url, song_filepath)
		pirate.mp3ify(song_name, song_filepath)
		pirate.track_record(song_name, song_artist, song_album, song_track, song_art_path)
		
		
		current_status += 1
		print(current_status)
		
	except Exception as e:
		pirate.error_tracker(e, function_name)
	
	
def thread_manager(things_assigned):
	# Manages the running of multiple threads so that stuff can be ran
	# Asynchonasouly with the time_looper
	
	function_name = "thread_manager"
	try:
		table = things_assigned[0]
		current_status = things_assigned[1]
		
		for i in range(0, len(table)-1):
			Thread(target=thread_ripper, args=[[table[i], current_status]]).start()
			print(i)
			# Adds a 10 second buffer before repeating
			time.sleep(10)
		
		# For when all the threads finish it will send a finshed signal
		current_status = -1
			
	except Exception as e:
		pirate.error_tracker(e, function_name)
	
	
def time_looper():
	# A continuous loop to print out the status every 2 minutes (120 seconds)
	
	function_name = "time_looper"
	
	try:
		while True:
			print(current_status)
			# The current status of the the downloads
			status = current_status
			
			# Exits the loop ending the program
			if (status == -1):
				break
				
			print(pirate.show_status(status, len_table))
			
			# Waits 2 minutes to repeat the function
			time.sleep(10)
			
	except Exception as e:
		pirate.error_tracker(e, function_name)


def start_threads():
	# Creates the Threads for running the two main threads
	thread_time = Thread(target=time_looper)
	thread_nest = Thread(target=thread_manager, args=[[table, current_status]])

	thread_time.start()
	thread_nest.start()


#########################################################
start_threads()
