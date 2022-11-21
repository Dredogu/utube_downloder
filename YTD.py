from pytube import Playlist
import os


url = input("Enter a url: ")
playlist = Playlist(url)
path = "<PATH>"  # C:\\Users\\

choice = int(input("Enter your choice: 1.Video 2.MP3 :  "))

i = 1

if choice == 1:
	for video in playlist.videos:
		print(f'{i}. {video.title} downloding...')
		video.streams.get_highest_resolution().download(path)
		i += 1
  
elif choice == 2:
    for music in playlist.videos:
        print(f'{i}. {music.title} downloding...')
        out = music.streams.filter(only_audio=True).first().download(path)
        base, ext = os.path.splitext(out)
        newfile = base + ".mp3"
        os.rename(out, newfile)
        i += 1
    
print("Done")
