# SoundTrack
Summary:
A group of Jupyter Notebooks that plays your music on a weekly schedule and shuffles song in between to fit the gaps. Written in Python3 and SQLite. It runs on Linux and plays to connected browser. Really cool Raspberry Pi (3 or higher) project.

Helpful Hints:
1. Use youtube-dl command line tool to populate shuffle folder(https://ytdl-org.github.io/youtube-dl/index.html)
  My config file looks like this:
  #Lines starting with # are comments
  #Always extract audio
  -x
  #use highest quality
  --audio-quality 0
  #mp3 only
  --audio-format mp3
  #remove spaces and special characters in file name
  --restrict-filenames
  #--get-filename -o '%(title)s.%(ext)s'
  -o '%(title)s.%(ext)s'
  
  For example(only use this tool on legally distributable content like Steadman and Creative Commons songs): 
  youtube-dl https://www.youtube.com/watch?v=ctCsZiQE_rQ
  [youtube] ctCsZiQE_rQ: Downloading webpage
  [youtube] ctCsZiQE_rQ: Downloading video info webpage
  [download] Destination: 4_Steadman_-_Good_To_Go.webm
  [download] 100% of 3.77MiB in 00:00
  [ffmpeg] Destination: 4_Steadman_-_Good_To_Go.mp3
  Deleting original file 4_Steadman_-_Good_To_Go.webm (pass -k to keep)

Todo (20190806):
1. Upload database creation scripts.
2. Get working over a smart phone browser(IPython.display.Audio autoplay non-functioning).
3. Get working in a Tesla browser through group nightly prayer to Tesla's update team to allow HTML 5 sound of any kind.

Special thanks to:

David Laganella - Master composer, virtuoso, author and professor.
  (https://en.wikipedia.org/wiki/David_Laganella)
  
Jackie Neale - Artist.(https://jackiephoto.photoshelter.com/index)  

Tim Seyfarth Garner - Musician, songwriter and producer.

Timmy Garner - Friend.

Concept:
Soundtrack is my ultimate mix tape for today. 

In 1985, for myself (but really for a specific friend), I might have created a 90 minute cassette tape as follows; to start the first 45 minute side I'd play a song that my friend and I share enthusiasm for, followed by 2-3 selections of songs that I thought my he/she doesn't know yet but would like just as much as our shared interest song, the rest of the side would be stuff I'm listening to in a semi-curated manner, ascending tempo to a climax at the latest the 40th minute and a slow song to end the side. A little blank space was acceptable at the end of the first side. 

The second 45 minute side of a mix tape cassette would start with a slammer, then songs I like currently with the same rise and fall of tempo/intensity as the first side. The final song would be my favorite slow song at the moment and inevitably it  would end with some blank space left on the cassette. That space is where I'd put my signature; usually a 30-40 second sample of David Brubeck, Mozart, Beethoven, Puccini, etc something classic, intensely sweet, and just as my friend might want another second the end of the cassete tape would go POP! Sorry gotta dig through older relative's record collections if you want to hear the rest of it. 

I'd play my mix tape any chance I could around the target friend and as soon as they said they liked any of it I'd eject it, give it to them and say "You can have it. I'll just make another."     

It's now 2019. We can connect to music from anywhere with an internet connection. We can tell precise time to the second. This is my week long "mix tape" that I'm making for myself, but also for you. I want to program your week based on what I think is probably appropriate music at appropriate times. You can add your songs to the suffle list or you can replace my scheduled songs with yours one-by-one. The end product is the same.


