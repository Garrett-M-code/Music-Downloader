# 7/9/2024
# A Program to download and convert Youtube videos into mp3 files

import Functions as pirate
from ODSReader import ODSReader


########################################################################

def thread_ripper(song):
	# Runs the completion loop for each individual item.
	
	function_name = "thread_ripper"
	
	try:
		song_name = (song[0]).strip()
		link_url = (song[1]).strip()
		song_filepath = song[2].strip()
		song_artist = song[3]
		song_album = song[4]
		song_track = song[5]
		song_art_path = song[6].strip()
		
		print("\n\t" + song_name + "\n")
		
		# Adds protection for blank options
		if (song_artist == None):
			song_artist = "Pass"
			
		if (song_album == None):
			song_album = "Pass"
			
		if (song_track == None):
			song_track = "Pass"
			
		song_path = "Music/" + song_filepath
		file_resource = str(song_path + "/" + song_name + ".mp3")
		
		try:
			pirate.reorganizer(song_filepath)
		except:
			pass
		
		# Defines import variables to be used with the different functions
		pirate.mp3ify(song_name, link_url, song_path)
		pirate.track_record(song_name, file_resource, song_artist, song_album, song_track, song_art_path)
		
	except Exception as e:
		pirate.error_tracker(e, function_name)

######################################################################


# Opens the file
document = ODSReader(u'fix.ods', clonespannedcolumns=True)

# Adds document data as a nested list. Rows First, Collumns Second.
table = document.getSheet(u'Sheet1')

# Length of the table
len_table = len(table)

for i in range(0, len_table):
	thread_ripper(table[i])
