# Music-Downloader
A python script used to read spreadsheets, scarpe music from youtube, and organize it. 

### Libraries used
 - pytubefix
 - ODSReader
 - Pillow
 - music_tag
 - odfpy

To operate the program, create a spreadsheet in the `.ods` format with the name 'list.ods'. 

 - The first collumn should be the file name
 - The second collumn should be the Youtube url
 - The third collumn should be the desired RELATIVE filepath
 - The fourth collumn should be the Artist
 - The fifth collumn should be the Albumn
 - The sixth collumn should be the track number
 - The seventh should be the path to artwork

Of this information, only the artist, albumn, and track are optional. You can technically run this program without artwork, however, you may run into issues.

### Errors

If you get an `HTTP 400: Bad Request Error`, this is an issue with pytubefix and Youtube client. Unfourtounantly, this is out the scope of this program to fix. To troubleshoot, ensure you are connected to internet, update pytubefix, or wait for the next update to pytubefix.

If you get an `The syntax of the command is incorrect.`, this means your filepath is incorrect. Either the artwork, or the file destination is incorrectly formatted in your spreadsheet.

Finally, you may have issues downloading songs marked as explicit or age rated. Unfourtounatly, this is on Youtube's end to control. Try finding the same song in a different video and test your results.