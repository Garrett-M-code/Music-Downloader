from pytube import YouTube
import music_tag
from PIL import Image

yt = YouTube('https://youtu.be/TPVs1heWJGY?si=rNeKfZ6sENKugl89')

stream = yt.streams.get_by_itag(139)
stream.download(output_path='test_music', filename='trust.mp3')

audio = music_tag.load_file("test_music/trust.mp3")
audio['title'] = "Trust Nobody"
audio['artist'] = "Hippie Sabatage"
audio['album'] = "Random"
audio['tracknumber'] = "3"


with open("art.jpg", 'rb') as img_in:
    audio['artwork'] = img_in.read()


art = audio['artwork']
art.first.thumbnail([64, 64])
art.first.raw_thumbnail([64, 64])


audio.save()
